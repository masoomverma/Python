print()
print()
print('Enter the student detail.')
print()
print()
school = input('Enter School Name: ')
name = input('Name: ')
std = input('Std.: ')
sec = input('Sec.: ')
roll_no = input('Roll No.: ')
print()
print()
print('Enter the marks.')
print()
print()
sub1 = int(input('Math: '))
sub2 = int(input('Science: '))
sub3 = int(input('S.S: '))
sub4 = int(input('English: '))
sub5 = int(input('Hindi: '))
a_b = int(sub1+sub2)
a_b_c = int(a_b+sub3)
a_b_c_d = int(a_b_c+sub4)
a_b_c_d_e = int(a_b_c_d+sub5)
per = float(a_b_c_d_e/500)
final_per = per*100
if (final_per >= 90):
    final_grade = 'A'
elif (final_per >= 80 and final_per < 90):
    final_grade = 'B'
elif (final_per >= 70 and final_per < 80):
    final_grade = 'c'
elif (final_per <= 70):
    final_grade = 'D'


# Printing Process

print()
print()
print('                                           ',
      school, '                                             ')
print()
print()
print()
print()
print('Name:', name)
print()
print('Std.:', std)
print()
print('Roll No.:', roll_no)
print()
print('Sec.:', sec)
print()
print()
print()
print()
print('--------------------------------------------------------------------------------------------------')
print('|                                         Subject Scores                                         |')
print('--------------------------------------------------------------------------------------------------')
print('|    Subject                       |       Total Marks         |          Obtained Marks         |')
print('--------------------------------------------------------------------------------------------------')
print('|    Math                          |',
      '          100             |', '               ', sub1, '              |')
print('--------------------------------------------------------------------------------------------------')
print('|    Science                       |',
      '          100             |', '               ', sub2, '              |')
print('--------------------------------------------------------------------------------------------------')
print('|    S.S                           |',
      '          100             |', '               ', sub3, '              |')
print('--------------------------------------------------------------------------------------------------')
print('|    English                       |',
      '          100             |', '               ', sub4, '              |')
print('--------------------------------------------------------------------------------------------------')
print('|    Hindi                         |',
      '          100             |', '               ', sub5, '              |')
print('--------------------------------------------------------------------------------------------------')
print()
print('                                                                                        Grade:', final_grade)
print()
print()
if (final_per >= 33):
    print('Percentage:', final_per,
          '                                                                                         ', 'Result: Pass')
else:
    print('Percentage:', final_per,
          '                                                                                         ', 'Result: Fail')
print()
print()
print()
print()
print('Class Teacher Sign                                                                                         Principal Sign ')
print()
print()
