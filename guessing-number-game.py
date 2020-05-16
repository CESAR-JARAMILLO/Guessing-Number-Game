# My Attempt
import random
number = random.randint(1,21)

name = input("Hello, what is your name? ")

print("Well, {}, I am thinking of a number between 1 and 20.".format(name))

guess = int(input("Take a guess. "))
count = 0

while guess != number:
  if guess > number:
    print("Your guess is too high")
    guess = int(input("Take a guess. "))
    count += 1
  elif guess < number:
    print("Your guess is too low.")
    guess = int(input("Take a guess. "))
    count += 1

print("Good job, {}! You guessed the number in {} guesses!".format(name,count))


import random


# Soloution
guessesTaken = 0

print("Hello, what is your name?")
myName = input()

number = random.randint(1,20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

for guessesTaken in range(6):
  print("Take a guess.")
  guess = input()
  guess = int(guess)

  if guess < number:
    print("Your guess is too low.")

  if guess > number:
    print("Your guess is too high.")

  if guess == number:
    break

if guess == number:
  guessesTaken = str(guessesTaken + 1)
  print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")

if guess != number:
  number = str(number)
  print("Nope. The number I was thinking of was " + number + ".")


# Use of:
# random module
# randint() function
# variables
# print() function
# input() function
# string concatination
# for statements
# str() and int() functions
# Booleans
# Comparison operators
# Conditions
# if statements
# break statements
# range() function
