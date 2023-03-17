import csv
import random
import re

def phn_gen():
    p=list('0000000000')
    p[0] = str(random.randint(1,9))
    for j in [1,2,6,7,8]:
        p[j] = str(random.randint(0,9))
    for k in [3,4]:
        p[k] = str(random.randint(0,8))
    if p[3]==p[4]==0:
        p[5]=str(random.randint(1,8))
    else:
        p[5]=str(random.randint(0,8))
    n = list(range(10))
    if p[6]==p[7]==p[8]:
        n.remove(int(p[6]))
    p[9] = str(random.choice(n))
    p = ''.join(p)
    return p[:3] + '-' + p[3:6] + '-' + p[6:]

def name_gen():
    first_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez"]
    return random.choice(first_names), random.choice(last_names)

def email_gen(name, surname):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "websense.com", "qaexch2010.wbsn"]
    name = name.lower()
    surname = surname.lower()
    domain = random.choice(domains)
    return f"{name}.{surname}@{domain}"

def cc_gen():
    visa_pattern = "4[0-9]{12}(?:[0-9]{3})?$"
    mastercard_pattern = "5[1-5][0-9]{14}"
    amex_pattern = "3[47][0-9]{13}"
    discover_pattern = "6(?:011|5[0-9]{2})[0-9]{12}"
    patterns = [visa_pattern, mastercard_pattern, amex_pattern, discover_pattern]
    pattern = random.choice(patterns)
    while True:
        cc_num = str(random.randint(10**15, 10**16-1))
        if re.match(pattern, cc_num):
            return cc_num

data = [["Name", "Surname", "Phone", "Email", "Credit Card Number"]]

for i in range(100):
    name, surname = name_gen()
    phone = phn_gen()
    email = email_gen(name, surname)
    cc_num = cc_gen()
    data.append([name, surname, phone, email, cc_num])

with open("customers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
