age = input("Enter your age: ")
if type(age) == str:
    print("You Get Free Beer")
elif age < 18:
    print('Go home my child')
else:
    print("No Beer For You")