from django.core import exceptions

def check_alphabetical_letters(value):
    for letter in value:
        if not letter.isalpha():
            raise exceptions.ValidationError("Only alphabetical letters are allowed.")