from django.shortcuts import render
import random
# Create your views here.



def generate_random_8_digit_number():
    return random.randint(10000000, 99999999)


random_number = generate_random_8_digit_number()
print("Random 8-digit number:", random_number)




