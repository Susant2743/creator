# -*- coding: utf-8 -*-
import requests
import uuid
import random
import time
from datetime import datetime
import base64
import json
import hashlib
import os
from faker import Faker
import string
import spintax


print('                Instagram Account Creator\n                 Telegram @NamasteHacker\n')


# Functions
def generate_uuid(prefix: str = '', suffix: str = '') -> str:
    return f'{prefix}{uuid.uuid4()}{suffix}'


def generate_android_device_id() -> str:
    return "android-%s" % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]


def generate_useragent():
    with open("UserAgent.txt", "r")as file:
        agents = file.read().splitlines()
        a = random.choice(agents)
        user = a.split(",")
    return f'Instagram 261.0.0.21.111 Android ({user[7]}/{user[6]}; {user[5]}dpi; {user[4]}; {user[0]}; {user[1]}; {user[2]}; {user[3]}; en_US; {user[9]})'


def get_mid():
    params = None
    api_url = f"https://i.instagram.com/api/v1/accounts/login"
    response = requests.get(api_url, params=params)
    mid = response.cookies.get("mid")
    if mid != None:
        return mid
    else:
        u01 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        us1 = str("".join(random.choice(u01)for k in range(int(8))))
        return f'Y4nS4g{us1}zwIrWdeYLcD9Shxj'


def Username():
    fake = Faker()
    name = fake.name()
    return str(name)


def Password():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all, 9)
    password = "".join(temp)
    return password


def generate_jazoest(symbols: str) -> str:
    amount = sum(ord(s) for s in symbols)
    return f'2{amount}'


def Birthday():
    day = str(random.randint(1, 28))
    month = str(random.randint(1, 12))
    year = str(random.randint(1988, 2003))
    birth = [day, year, month]
    return birth

def DP():
    directory = r'Data/DP/'
    files = os.listdir(directory)
    random_file = random.choice(files)
    file_path = os.path.join(directory, random_file)
    return file_path

def Posts():
    posts = []
    directory = r'Data/Posts/'
    files = os.listdir(directory)
    for i in range(3):
        random_file = random.choice(files)
        file_path = os.path.join(directory, random_file)
        posts.append(file_path)
    return posts
    



# Veriables
BlockVersion = 'a399f367a2e4aa3e40cdb4aab6535045b23db15f3dea789880aa0970463de062'
App_ID = '567067343352427'

Device_ID = generate_uuid()
Family_ID = generate_uuid()
Android_ID = generate_android_device_id()
UserAgent = generate_useragent()
X_Mid = get_mid()
adid = str(uuid.uuid4())

water = str(uuid.uuid4())