import random
import string

def pass_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += random.choice(characters)
        if(password==',' or password=="'"):
            continue
    return password
pass_length = int(input("enter range of password: "))
print(pass_generate(pass_length))