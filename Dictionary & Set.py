# Dictionary.

mark = {}
inp1 = input('Sub 1: ')
inp2 = input('Marks: ')
mark[inp1] = inp2
Q = input('Do you want to add new data to marks (Yes = y): ')
ans = 'y'
if (Q == ans):
    inp1 = input('Sub 2: ')
    inp2 = input('Marks: ')
    mark[inp1] = inp2
    if (Q == ans):
        a = input('Do you want to add new data to marks (Yes = y): ')
        ans = 'y'
        if (a == ans):
            inp1 = input('Sub 3: ')
            inp2 = input('Marks: ')
            mark[inp1] = inp2
            b = input('Do you want to add new data to marks (Yes = y): ')
            ans = 'y'
            if (b == ans):
                inp1 = input('Sub 4: ')
                inp2 = input('Marks: ')
                mark[inp1] = inp2
                print(mark)
elif ():
    print('Thank You.')

# Set.
print()
print()
print()
sub = {'java', 'python', 'c++', 'python', 'java',
       'javascript', 'C', 'java', 'python', 'c++', 'C'}
print(sub)
print(len(sub))

# Saving value of both 9 and 9.0:

value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)
