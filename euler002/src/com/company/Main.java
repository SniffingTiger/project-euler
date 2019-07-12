package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        boolean end = false;

        System.out.println("This console app prints out the sum of the even numbers in the Fibonacci sequences that precedes any given number.");

        while (end != true) {
            System.out.print("\nEnter any number here: ");

            Scanner in = new Scanner(System.in);
            int num = in.nextInt();

            System.out.println("The sum of all the even members of the Fibonacci sequence that precedes " + num + " is: " + sumOfEvenFibonaccis(num));
            System.out.print("\nInput any key to go again or input \"Exit\" to leave: ");
            String endOrNah = in.next();
            if (endOrNah.equalsIgnoreCase("Exit")) {
                end = true;
            }
        }
    }

    private static int sumOfEvenFibonaccis(int num) {
        int sumOfEvens = 0;
        int previousFibonacci = 1;
        for (int i = 2; i < num; ) {
            if (i % 2 == 0) {
                sumOfEvens += i;
            }
            int currentFibonacci = i;
            i += previousFibonacci;
            previousFibonacci = currentFibonacci;
        }

        return sumOfEvens;
    }
}