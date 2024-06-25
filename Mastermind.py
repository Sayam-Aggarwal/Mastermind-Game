# Mastermind Game
import random

n = random.randint(1000,10000)
guess = input("Guess the 4 digit number: ")
number_guess = 1
right_digit = 0

if guess == n:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    while guess != n:
        num = str(n)
        right = ["X", "X", "X", "X"]
        for i in range(len(num)):
            if guess[i] == num[i]:
                right[i] = num[i]
                right_digit += 1
        if right_digit < 4:
            print(f"Not quite the number. But you did get {right_digit} digit(s) correct!")
            right_digit = 0
            print("Also these numbers in your input were correct.")
            print(right)
            guess = input("Enter your next choice of numbers: ")
            number_guess += 1
        elif right_digit == len(num):
            print(right)
            print("You've become a Mastermind.")
            print(f"It only took you {number_guess} tries")