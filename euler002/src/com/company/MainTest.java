package com.company;

import org.junit.Test;

import static com.company.Main.*;
import static org.junit.Assert.*;

public class MainTest {
    @Test
    public void sumOfEvenFibonaccisTest() {
        // Declare test variables
        int input1 = 10;
        int result1 = 10;

        int input2 = 60;
        int result2 = 44;

        assertEquals(result1, sumOfEvenFibonaccis(input1));
        assertEquals(result2, sumOfEvenFibonaccis(input2));
    }
}