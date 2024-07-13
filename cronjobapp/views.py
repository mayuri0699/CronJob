from django.shortcuts import render
import logging
import random


def generate_random_8_digit_number():
    return random.randint(10000000, 99999999)

logger = logging.getLogger(__name__)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Random 8-digit number:")

