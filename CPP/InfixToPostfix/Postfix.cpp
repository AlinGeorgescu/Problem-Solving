#include <iostream>
#include <stack>
#include <string>

using std::cin;
using std::cout;
using std::stack;
using std::string;

inline unsigned short priority(const char c) {   
    if (c == '^' || c =='|' || c == '&') {
        return 3; 
    }

    if (c == '*'|| c == '/') {
        return 2;
    }

    if (c == '+' || c == '-') {
        return 1;
    }
}

inline bool isDigit(const char c) {
    return (c >= '0' && c <= '9');
}

inline bool isOperator(const char c) {
    if (c == '^' || c =='|' || c == '&' || c == '*' ||
        c == '/' || c == '+' || c == '-') {
        return true; 
    }

    return false;
}

int main() {
    int i = 0;
    char input[255];
    string result;
    stack<char> stack;

    fgets(input, 255, stdin);

    while (input[i] != '\0') {
        cout << input[i] << '\n';
        if (isDigit(input[i])) {
            // Add numbers to the postfix form.
            result.push_back(input[i]);

            // If the number is finished add space.
            if (!isDigit(input[i + 1])) {
                result.push_back(' ');
            }
        } else if (input[i] == '(') {
            stack.push(input[i]);
        } else if (input[i] == ')') {
            // Extract every operator in the parenthesis.
            while (stack.top() != '(') {
                char c = stack.top();
                stack.pop();

                result.push_back(c);
                result.push_back(' ');
            }

            // Extract and do not print the left bracket.
            stack.pop();
        } else if (isOperator(input[i])) {
            char O1 = input[i];

            // Print operators with lower priority.
            if (!stack.empty()) {
                char O2 = stack.top();

                while (isOperator(O2) && (priority(O1) <= priority(O2))) {
                    stack.pop();
                    result.push_back(O2);
                    result.push_back(' ');

                    if (!stack.empty()) {
                        O2 = stack.top();
                    }
                }
            }

            stack.push(O1);
        }

        ++i;
    }

    // Print the other signs.
    while (!stack.empty()) {
        char c = stack.top();
        stack.pop();

        result.push_back(c);
        result.push_back(' ');
    }

    cout << result << '\n';

    return 0;
}