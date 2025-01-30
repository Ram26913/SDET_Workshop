a = input("Enter a number: ")
b = input("Enter a number: ")
print("sum is" + str(int(a)+int(b)))# type casting string to integer
print("difference is" + str(int(a)-int(b)))
print("product is" + str(int(a)*int(b)))

if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a is equal to b")