from random import *
print()
print("Welcome to our Guessing number Application")
print("--"*30)
attempt=0
n=randint(1,100)
while True:
    guess = int(input("Enter your guess..[1-100]: "))

    if guess == n:
        attempt = attempt+1
        print(f"Congratulations!!!! You have guessed it correctly in {attempt} attempts")
        break
    elif guess<n:
        print("value is greater...")
        attempt = attempt+1
    else:
        print("value is less...")
        attempt = attempt+1
        
    print("--"*30)
    print()