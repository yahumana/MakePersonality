from random import randint


def make_password(length=16):
    return ''.join(chr(randint(44, 126)) for i in range(length))

