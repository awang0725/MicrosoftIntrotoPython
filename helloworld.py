# print('hello world!')

first_name = input("please input your first name:")
last_name = input("Please input your last name:")

# print(first_name)
# print(last_name)
# print("Hello " + first_name.capitalize() + " " + last_name.capitalize())

# print("original values")
# print(first_name)
# print(last_name)

# output = "Hello, " + first_name + " " + last_name
# output = "Hello, {} {}".format(first_name.capitalize(),last_name.capitalize())
output = "Hello, {0} {2} ".format(first_name,last_name)
print(output)