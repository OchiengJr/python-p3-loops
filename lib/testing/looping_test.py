#!/usr/bin/env python3

from looping import happy_new_year, square_integers, fizzbuzz

import io
import sys

class TestHappyNewYear:
    '''happy_new_year() in looping.py'''

    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            happy_new_year()
        finally:
            sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
        
        # answer.split(\n) produces a list that ends in ''
        answer_list = answer.strip().split('\n')
        # Last value should be the HNY string
        assert answer_list[-1] == "Happy New Year!", "Your final line does not match 'Happy New Year!', check spelling/capitalization!"
        digit_strings = [str(i) for i in range(10, 0, -1)]
        missing_digits = [i for i in digit_strings if i not in answer_list]
        assert not missing_digits, f"You didn't print all digits 10-1, missing {', '.join(missing_digits)}"


class TestSquareIntegers:
    '''square_integers() in looping.py'''

    def test_square_integers(self):
        '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
        assert(square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25])
        assert(square_integers([-1, -2, -3, -4, -5]) == [1, 4, 9, 16, 25])


class TestFizzBuzz:
    '''fizzbuzz() in looping.py'''

    def test_prints_1_to_100_fizzbuzz(self):
        '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            fizzbuzz()
        finally:
            sys.stdout = sys.__stdout__
        answer = captured_out.getvalue().strip()
        assert answer, "Nothing printed! Check your loop condition. Also, do you have print statements?"
        assert "Fizz" in answer, "The string 'Fizz' not found in your answer, check spelling/capitalization!"
        assert "Buzz" in answer, "The string 'Buzz' not found in your answer, check spelling/capitalization!"
        
        expected_output = []
        for i in range(1, 101):
            if i % 15 == 0:
                expected_output.append("FizzBuzz")
            elif i % 3 == 0:
                expected_output.append("Fizz")
            elif i % 5 == 0:
                expected_output.append("Buzz")
            else:
                expected_output.append(str(i))
        
        actual_output = answer.split('\n')
        for expected, actual in zip(expected_output, actual_output):
            assert expected == actual, f"Expected {expected}, but got {actual}"
        
        assert len(actual_output) == 100, f"Only looped {len(actual_output)} times, should have looped 100 times. Check your loop condition!"
