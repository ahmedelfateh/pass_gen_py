import random
import string
import os
import hashlib
import json

# MASTER_PASS=os.environ.get('MASTER_PASS')

def generate(platform, user, length, master_pass):
    # random.seed(platform+user+MASTER_PASS)
    random.seed(platform+user+master_pass)
    letters=string.ascii_letters + string.digits + "@$*&#"
    password=""
    length = int(length)
    for i in range(length):
        password+=random.choice(letters)
    
    web_pass = { "web_pass" : [{
        "platform":platform,
        "pass": password
        }]
        }

    new_pass = {
        "platform":platform,
        "pass": password
        }


    if not os.path.isfile('./pass.json'):
        with open("pass.json", 'a') as f:
            json.dump(web_pass, f)
    else:
        with open("pass.json", 'r') as f:
            data = json.load(f)
            data["web_pass"].append(new_pass)
        with open("pass.json", "w") as f:
            json.dump(data, f)

    print("your " + platform + " pass is: " + password)
    return password

def hash_pass(password):
    salt = os.urandom(32) # Remember this
    password = password

    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )

    print(key)
    return key

def save(pass_data):
    pass

platform = input("What is your platform? ")
user = input("What is your user? ")
length = input("What is your length? ")
master_pass = input("What is your master_pass? ")

password = generate(platform, user, length, master_pass)

hash_pass(password)