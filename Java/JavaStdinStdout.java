package com.main;

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        // read 3 ints and print them
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(a + "\n" + b + "\n" + c);
        scan.close();
    }
}
