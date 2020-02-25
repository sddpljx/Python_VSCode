import requests, random

def send_fish(name,password):
    header = {
        'user-agent' : 'Mozilia/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'referer' : 'https://lol-gams.website/lolm?agency=61'
    }
    data = {
        'u' : name,
        'p' : password,
        'agency' : '61'
    }

    url = 'https://lol-gams.website/lolm?agency=61'
    r = requests.post(url,data,headers=header)
    print(type(r.status_code), r.status_code)

for i in range(1,10000):
    name = str(random.randint(123456789,9999999999))
    password = ''.join(random.sample('qwertyuiop[asdfghjkl',random.randint(8,12)))
    password += ''.join(random.sample('1234567890',random.randint(0,3)))
    print(i,name,password)
    send_fish(name,password)