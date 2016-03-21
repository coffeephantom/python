# -*- coding: utf-8 -*-

import string
import random

def generate_copoun():
    copoun_list = []
    element = []
    character = string.ascii_letters
    digit = string.digits
    for letter in character:
        element.append(letter)

    for num in digit:
        element.append(num)
    print element
    
    for i in range(0, 200):
        copoun = ''
        for count in range(0, 15):
            copoun += random.choice(element)
        if copoun not in copoun_list:
            copoun_list.append(copoun)
    
    return copoun_list

print generate_copoun()