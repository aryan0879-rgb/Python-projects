
password = "aryan123"
tries = 1
a = input("Enter your password: ")

while a != password:
    tries += 1
    if tries > 3:
        print("False person")
        break
    a = input("Try again: ")

if a == password:
    print("You guessed it right!")
