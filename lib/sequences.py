#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci_sequence = []

    for i in range(length):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)
