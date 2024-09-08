# Acending

start = 1
while start <= 10:
    print(start)
    start += 1

print()

# Decending

print()
start = 10
while start >= 1:
    print(start)
    start -= 1
print()

# Print the multipliaction table of a number 'n'.

print()
n = int(input("Enter the number for it's table: "))
t = 1
while t <= 10:
    print(n*t)
    t += 1
print()

# Print square of the of the no. based on user choise.

print('Method-1')
print()
f = int(input('From: '))
t = int(input('To: '))
while f <= t:
    print(f*f)
    f += 1
# OR

print()
print('Method-2')
print()
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(num):
    print(num[i])
    i += 1
print()

# Search for a number x in this tuple using loop:

print()

# (Break Command)

print()
x = int(input('Enter number you want to find: '))
i = 0
while i < len(num):
    if (num[i] == x):
        print('Founded', x, 'at index:', i)
        break
    else:
        print('Finding')
    i += 1
print()

# To remove number x in this tuple using loop:

print()

# (Continue Command)

print()

e = int(input('How many input do you want to print: '))
r = int(input('Enter number you want to remove: '))
while i <= e:
    if (i == r):
        i += 1
    print(i)
    i += 1

# For Even No.

s = 1
print('Even No.')
print()
while s <= e:
    if (s % 2 != 0):
        s += 1
        continue
    print(s)
    s += 1

# For Odd No.

print('Odd No.')
print()
while s <= e:
    if (s % 2 == 0):
        s += 1
        continue
    print(s)
    s += 1
