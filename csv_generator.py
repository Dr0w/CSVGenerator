import csv
import random
import re


# #generates US phone number, rules:
# The area code cannot start with a zero,
# None of the middle three digits can be a 9,
# Middle three digits cannot be 000,
# Last 4 digits cannot all be the same.


def phn_gen():
    p = list('0000000000')
    p[0] = str(random.randint(1, 9))
    for j in [1, 2, 6, 7, 8]:
        p[j] = str(random.randint(0, 9))
    for k in [3, 4]:
        p[k] = str(random.randint(0, 8))
    if p[3] == p[4] == 0:
        p[5] = str(random.randint(1, 8))
    else:
        p[5] = str(random.randint(0, 8))
    n = list(range(10))
    if p[6] == p[7] == p[8]:
        n.remove(int(p[6]))
    p[9] = str(random.choice(n))
    p = ''.join(p)
    return p[:3] + '-' + p[3:6] + '-' + p[6:]


# generates Name and Surname from dictionary
def name_gen():
    first_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez",
                  "Martinez"]
    return random.choice(first_names), random.choice(last_names)


# generates email address by concatenating name and surname to lowercase combining with dot and dictionary of domains
def email_gen(name, surname):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    name = name.lower()
    surname = surname.lower()
    domain = random.choice(domains)
    return f"{name}.{surname}@{domain}"


# randomly generates CC numbers by regex patterns, available vendors: Visa, MC, AMEX, Discovery
def cc_gen():
    visa_pattern = "4[0-9]{12}(?:[0-9]{3})?$"
    mastercard_pattern = "5[1-5][0-9]{14}"
    amex_pattern = "3[47][0-9]{13}"
    discover_pattern = "6(?:011|5[0-9]{2})[0-9]{12}"
    patterns = [visa_pattern, mastercard_pattern, amex_pattern, discover_pattern]
    pattern = random.choice(patterns)
    while True:
        cc_num = str(random.randint(10 ** 15, 10 ** 16 - 1))
        if re.match(pattern, cc_num):
            return cc_num


# CSV Column structure
data = [["Name", "Surname", "Phone", "Email", "Credit Card Number"]]

# Main generation part, range sets number of records
for i in range(1000):
    name, surname = name_gen()
    phone = phn_gen()
    email = email_gen(name, surname)
    cc_num = cc_gen()
    data.append([name, surname, phone, email, cc_num])

# writes generated data into csv file at the same folder where script is located
filename = f"customers_{len(data) - 1}.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
