# Print the table of the user based choise.


n = int(input('Enter the no."n": '))
i = 1
while i <= n:
    print(i*n)
    i += 1

# Print the sum of first 'n' natural no. of the user based choise.

# By While Loop
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print('Sum of first natural no.:', s)

# Print the elements in the list obtain by the user For Loop.
num = []
num.append(input('Enter No. to add in the list: '))
inp = input('Do you want to print more no. (y/n): ')
Q = 'y'
while inp == Q:
    print('OK')
    num.append(input('Enter No. to add in the list: '))
    inp = input('Do you want to print more no. (y/n): ')
    if (Q != inp):
        print('OK')
print(num)

# Print the factorial of the first 'n' natural no.

fact = 1
for el in range(1, n+1):
    fact *= el
print('The factorial of the "n":', fact)
