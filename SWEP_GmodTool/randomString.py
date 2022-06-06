

from random import randrange

import random

def randomString():
    stringLenght = random.randrange(1, 10)

    stringResult = ""

    for i in range(stringLenght):
        chara = (chr(random.randrange(97, 123)))
        stringResult += chara

    return stringResult
