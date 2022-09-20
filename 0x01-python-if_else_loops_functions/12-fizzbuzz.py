#!/usr/bin/python3
def fizzbuzz():
    s = ["{:d}", "Fizz", "Buzz", "FizzBuzz"]
    for x in range(1, 101):
        print(s[(x % 3 == 0) + 2 * (x % 5 == 0)].format(x), end=' ')
