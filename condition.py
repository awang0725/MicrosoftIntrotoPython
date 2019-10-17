# # single condition demo
# price = float(input('Please enter how much you paied: '))

# if price >= 1.00:
#     tax_rate = 0.07
# else:
#     tax_rate = 0

# print('You should pay tax: ' + str(price*tax_rate))



# multiple conditions demo

gpa = float(input('Please enter your GPA: '))
lowest_grade = float(input('Please enter your lowest grade: '))

if gpa >= 0.80 and lowest_grade >= 0.7:
    # print('Wonderful Job, you made the honor roll')
    honor_roll = True
else:
    # print('You are not qualified for a honor roll')
    honor_roll = False


if honor_roll:
    print('Wonderful job! You made the honor roll')
else:
    print('You are not quailified for an honor roll')