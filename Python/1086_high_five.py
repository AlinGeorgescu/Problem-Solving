#!/usr/bin/env python3

import ast

def push_mark(mark : int, student_id : int, students : dict) -> None:
    if student_id in students:
        student_marks = students[student_id]

        i = 0
        while i < len(student_marks) and student_marks[i] > mark:
            i += 1

        if len(student_marks) < 5:
            student_marks.append(mark)

        if i < len(student_marks) - 1:
            for j in range(len(student_marks) - 1, i, -1):
                student_marks[j] = student_marks[j - 1]

            student_marks[i] = mark

    else:
        students[student_id] = [mark]

def main() -> None:
    items = ast.literal_eval(input("Enter items: "))

    students = {}

    for student_id, mark in items:
        push_mark(mark, student_id, students)

    res = [[student_id, sum(students[student_id]) // len(students[student_id])] \
                for student_id in students]
    print(res)

if __name__ == "__main__":
    main()
