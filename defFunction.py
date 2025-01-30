def factorial(n):
    result=1
    for i in range(1,n+1):
        result *=i
        print("Factorial of the number:" + str(result))

# while True:
#     n = input("Enter a number: ")
#     if (n.isdigit()):
#      factorial(n)
#      break
#     else:
#      print("Enter Valid number")
