import random
import string

def get_random_string(length):
    lowercase = string.ascii_lowercase 
    uppercase = string.ascii_uppercase
    number = string.digits
    letters = uppercase + lowercase + number
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

s1 = get_random_string(6)
s2 = get_random_string(6)
s3 = get_random_string(6)

print("Password: \n" + s1 + '-' + s2 + '-' + s3)