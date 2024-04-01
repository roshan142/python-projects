#Number guessing 01/04/24
import random
print("Welcome To Number Guessing Game!")
number = input("Enter a Number upto which an random number will generate:")
if number.isdigit():
    number = int(number)
    if number <= 0:
        print("Enter a number greater than Zero Next Time!")
        quit()
else:
    print("Please Type A Number Next Time!")
    quit()      
random_num = random.randint(0,number)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Enter Your Guess:")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number Next Time!")
        continue
    if user_guess == random_num:
        print("You Got it!")
        break
    elif user_guess > random_num:
        print("You were Above the number:")
    else:
        print("You were Below the number:")     
print(f"You Got it in {guesses} Guesses!")





