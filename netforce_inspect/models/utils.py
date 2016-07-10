import random, string

def get_random(length=8, only_number=False, letter=""):
    #chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    #chars = string.ascii_letters + string.digits
    chars = string.ascii_lowercase+string.digits
    if only_number:
        chars = string.digits
    elif letter:
        chars = "eff"+string.digits
    #chars = string.digits
    rnd = random.SystemRandom()
    res=''.join(rnd.choice(chars) for i in range(length))
    print("RANDOM : ", res)
    return res
