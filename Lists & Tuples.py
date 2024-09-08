# 1. Program based on user choise.

name1 = input('Movie 1: ')
name2 = input('Movie 2: ')
name3 = input('Movie 3: ')
list = [name1, name2, name3]
print(list)

# OR

movie = []
movie.append(input('Movie 1: '))
movie.append(input('Movie 2: '))
movie.append(input('Movie 3: '))
print(movie)


# 2. WAP to check if a list contains a palindrome of elements. (Hint: Use copy() method).

list = []
list.append(input('Input 1: '))
list.append(input('Input 2: '))
list.append(input('Input 3: '))
main_list = list
copy_list = main_list.copy()
copy_list.reverse()
if (copy_list == main_list):
    print('The list is Palindrome.')
else:
    print('The list is not Palindrome.')

# WAP tp count the number of the students in a tuple.

student_grade = []
print('# System can take 10 input at one time.')
student_grade.append(input('Student 1: '))
student_grade.append(input('Student 2: '))
student_grade.append(input('Student 3: '))
student_grade.append(input('Student 4: '))
student_grade.append(input('Student 5: '))
student_grade.append(input('Student 6: '))
student_grade.append(input('Student 7: '))
student_grade.append(input('Student 8: '))
student_grade.append(input('Student 9: '))
student_grade.append(input('Student 10: '))
grade_count = student_grade.count(input('Grade: '))
print(grade_count)

# Sorting the grade list.

print('Do you want to sort the list.')
str = 'Y'
Q = input('Yes(Y)/No(N): ')
if (Q == str):
    student_grade.sort()
    print(student_grade)
else:
    print('Thank You')
