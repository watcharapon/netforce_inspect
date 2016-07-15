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

def get_random_ip_address(self,limit=10):
    items=[]
    digit=[]
    for i in range(limit):
        while 1:
            d=int(random.random()*100)
            if d not in digit:
                digit.append(d)
                break
        ip="192.168.%s.%s"%(d%2,d)
        item=[ip,ip]
        items.append(item)
    return items

def get_random_max_address(self,limit=10):
    items=[]
    digit=[]
    digit2=[]
    for i in range(limit):
        while 1:
            d=str(int(random.random()*100)).zfill(2)
            if d not in digit:
                digit.append(d)
                break
        while 1:
            d2=str(int(random.random()*10)).zfill(2)
            if d2 not in digit2:
                digit2.append(d2)
                break
        chars = string.ascii_lowercase
        digits = string.digits
        between=""
        rnd = random.SystemRandom()
        for i in range(4):
            c=rnd.choice(chars)
            d3=rnd.choice(digits)
            between+="%s%s:"%(c,d3)
        max_addr="%s:%s%s"%(d,between,d2)
        item=[max_addr,max_addr]
        items.append(item)
    return items
