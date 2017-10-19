from secrets import choice
import string


def generate_random_string(size):
    return ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(size)])