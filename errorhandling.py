x = 42
y = 0

try:
    print(x / y)
except ZeroDivisionError as e:
    print(e)
else:
    print('something else is wrong')
finally:
    print('final part of your code to cleanup')

# print(x / y)