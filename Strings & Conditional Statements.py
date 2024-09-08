# Program printing the user choise words.

str = input('Input: ')
print(str)

# Now printing the length of the Input from the above.

length = len(str)
print('The Input Contain', length, 'words.')
print("# The result contain the 'space' as a unique character.")

# Write the program to the find the letter contain in the input.

print('Do you want to find the location of the letter from the input.')
str1 = 'Y'
str2 = 'N'
Q = input('Yes(Y) / No(N): ')
if (Q == str1):
    search = input('Find: ')
    print('The location of the word:', str.find(search))
    print("The '0' is unique location, represent the starting.")

elif (Q == str2):
    print('Thank you for checkiing the program.')


# If statment like wehther condition 1 or condition 2.

age = int(input('Age: '))
if (age >= 18):
    print('You are allowed for the test of the driving licence.')
elif (age != 18):
    print('You are not allowed to take the driving licence test.')

# Even and Odd Program.

i = int(input('Number: '))
r = i % 2
# Or just rplace the 'i' by (i % 2) and remove the 'r'.
if (i == 0):
    print('The input number is Even.')
else:
    print('The input number is Odd.')

# Finding th bigger no. b/w the 3 no's.

a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))
if (a > b and a > c):
    print('Number', a, 'is greater than', b, ',', c, ".")
elif (b > c):
    print('Number', b, 'is greater than', a, ',', c, ".")
else:
    print('Number', c, 'is the greatest.')

# Checking whether a number is a multiple of 7 or not.

num = int(input('Input: '))
r = (num % 7)
if (r == 0):
    print('The number is a multiple of 7.')
else:
    print('The number is not a multipe of 7.')
