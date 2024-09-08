# integer is for whole no. and float is for decimal

# Arithematic Operators:.
# Addition          : (a+b) or (a + b)
# Subtaction        : a-b
# Multiplication    : a*b
# Division          : a/b
# Floor Division    : a//b (It give the digit which is ahead of the deciamal lie=ke if we if get our ans after dividing a by b in format of  c.df then it give the value c.)
# Exponent          : a**b
# Modulus           : a%b (It give the digit which just left as reminder after dividing a by b.)

# START

# print(3 % 2)


# 1. User choise sum:

first = int(input('a : '))
second = int(input('b : '))
print('The sum is : ', first + second)

# 2. Area of a square choise based on the user:

print('# For the area of the square i need some information.')
side = float(input('Side : '))
print('Area of the square is :', side*side)

# 3. Average of the two floating number:

first = float(input('a : '))
second = float(input('b : '))
# sum = first + second                        # With line no. 33 or simply by only line no. 34 both will give same ans but if we use line no. 33 then on line no. 34 we only just have to use sum in the place of the first + second.)
print('Average is :', (first + second) / 2)

# 4. Print True in case of 'a' greater than or equal to 'b'. If not then print False.

first = float(input('a : '))
second = float(input('b : '))
print('Result :', first >= second)
