<<<<<<< HEAD
#Create a function named `hello_devops` that prints `I am learning DevOps`. Call the function once.

#def hello_devops():
#   print("i am learning devops")
#hello_devops()

#Create a function named `greet` that accepts a `name` and prints `Welcome` followed by that name. Call it with `Rutik`.

#def greet(name):
#    print("welcome",name)
#greet("rutik")

#Create a function named `add_numbers` that accepts two numbers and returns their sum. Call it with 5 and 10, then print the result.

#def add_numbers(a,b):
#    sum1=a+b
#    print("sum is ",sum1)
#add_numbers(5,10)

def add_numbers(a, b):
    sum1 = a + b
    return sum1

result = add_numbers(5, 10)
print("Sum is", result)


#Create a function `check_disk_usage(usage)`: return `Critical` for usage >= 90, `Warning` for usage >= 70, otherwise `Normal`. Test it with 95.

def check_disk_usage(usage):
    if usage>=90:
        print("critical")
    elif usage>= 70:
        print("warning")
    else:
        print("normal")
=======
#Create a function named `hello_devops` that prints `I am learning DevOps`. Call the function once.

#def hello_devops():
#   print("i am learning devops")
#hello_devops()

#Create a function named `greet` that accepts a `name` and prints `Welcome` followed by that name. Call it with `Rutik`.

#def greet(name):
#    print("welcome",name)
#greet("rutik")

#Create a function named `add_numbers` that accepts two numbers and returns their sum. Call it with 5 and 10, then print the result.

#def add_numbers(a,b):
#    sum1=a+b
#    print("sum is ",sum1)
#add_numbers(5,10)

def add_numbers(a, b):
    sum1 = a + b
    return sum1

result = add_numbers(5, 10)
print("Sum is", result)


#Create a function `check_disk_usage(usage)`: return `Critical` for usage >= 90, `Warning` for usage >= 70, otherwise `Normal`. Test it with 95.

def check_disk_usage(usage):
    if usage>=90:
        print("critical")
    elif usage>= 70:
        print("warning")
    else:
        print("normal")
>>>>>>> ac1f4c229790b8a0eee65b5f616d2b8066b3e578
check_disk_usage(95)