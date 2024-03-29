# Programming Language used : Python

def input_numbers():
    a, b = map(int, input("Enter two non-zero positive integers: ").split())
    
    if a <= 0 or b <= 0:
        print("Your inputs are not valid! Please enter two non-zero positive integers.")
    else:
        input_range = list(range(a, b+1))
        odd = []
        even = []
        
        #indirect function call using lambda functions
        seperate_function(lambda x: even.append(x) if x % 2 == 0 else odd.append(x), input_range)
        print("odd numbers: ", odd)
        print("Even numbers: ", even)
        
        operation = input("Enter operation (add_even, add_odd or, add_all): ")
        if(operation == "add_even" or operation == "add_odd" or operation == "add_all"):
            result = return_calculation(operation, even, odd)
            print("Result of operation " + str(operation) + " is: " + str(result))
        else:
            print("Invalid operation!")
    
# seperate_function calls another function (my_function) indirectly
def seperate_function(my_function, numbers):
    for element in numbers:
        my_function(element)
        
def return_calculation(operation, odd, even):
    
    #function calls within another function(indirect)
    if operation == "add_even":
        return add(even)
    elif operation == "add_odd":
        return add(odd)
    elif operation == "add_all":
        return add(even) + add(odd)
    else:
        return "Invalid operation!"

def add(numbers):
    total = 0
    for element in numbers:
        total += element
    return total

input_numbers()
