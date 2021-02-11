import re

phoneregex = regex = re.compile(r'\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})')

emailregex = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')

phone_numbers = []
lines = []
emails = []

file2read = open('potential-contacts.txt', 'r')
# print(file2read)
for text in file2read:
    lines.append(text)

for line in lines:
    if emailregex.search(line):
        email = emailregex.search(line)
        grpemail = email.group()
        emails.append(grpemail)
    
file2read.close()

# print(emails)

newnumlist = []


for line in lines:
    number = phoneregex.search(line)
    # print(number)
    # grpby = number.group()
    # print(grpby)
    if number != None:
        grpby = number.group()
        newnumlist.append(grpby)
# print(newnumlist)
newnewlist = []

for numbers in newnumlist:
    fixednum = numbers.replace('.', '-')
    newnewlist.append(fixednum)

final_num_num = []

for numnum in newnewlist:
    if len(numnum) < 12:
        final_num_num.append(f'{numnum[:3]}-{numnum[3:6]}-{numnum[6:]}')
            # numnumnum = numnum.insert(3, '-')
            # print(numnumnum)

for j in newnewlist:
    if len(j) > 10:
        final_num_num.append(j)

print(emails)

final_num_num.sort()
emails.sort()
# print(final_num_num)

with open('phone_numbers.txt', 'w+') as f:
    for numbers in final_num_num:
        f.write(f'{numbers}\n')



with open('emails.txt', 'w+') as f:
    for email in emails:
        f.write(f'{email}\n')

















# for num in phone_numbers:
#     # print(num)
#     if len(num[0]) > 3:
#         print(num)
        # fixed = list(num[0].remove('-'))
        # print(fixed)
        # newnumlist.append(fixed)
# print(newnumlist)