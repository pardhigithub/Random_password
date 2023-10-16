import random
import string

def generate_pass(length, upperCase, lowerCase, Digits, SpecialCharactors):
    characters = ""
    if upperCase:
        characters += string.ascii_uppercase
    if lowerCase:
        characters += string.ascii_lowercase
    if Digits:
        characters += string.digits
    if SpecialCharactors:
        characters += string.punctuation
    if not characters:
        return "no characters selected: "
    

    password = ""
    for _ in range(length):
        password+=random.choice(characters)
    return password

length = int(input("enter length: "))
upperCase = input("upperCase yes: ").lower() == "y"
lowerCase = input("lowerCase yes: ").lower() == "y"
Digits = input("Digits yes: ").lower() == "y"
SpecialCharactors = input("SpecialCharactors yes: ").lower() == "y"

print(generate_pass(length, upperCase, lowerCase, Digits, SpecialCharactors))

