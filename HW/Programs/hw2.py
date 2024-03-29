import random

def input_numbers():
    # take 3 input from the user and store them in variables x, y and z
    x, y, z = map(int, input("Enter three non-zero positive integers: ").split())
    
    # checking if any input is zero or, if the first two inputs are the same 
    if x <= 0 or y <= 0 or z <= 0 or x == y:
        print("Please provide three non-zero, positive integers (First two input can't be the same)")
    else:
        expressions = bol_exp(x, y, z)
        
        # Generating a runtime error if the third input does not satisfy any expression and terminate
        if not expressions:
            raise RuntimeError(f"{z} is not divisible by numbers between {x} and {y} without a remainder")
            
        print("These are the available expressions that satisfy the conditions :")
        for exp in expressions:
            print(f"{z} % {exp} == 0")
        
        # Calling the function which randomly chooses a expression to execute     
        loop_guarded_command(x, y, z, expressions)
               

def bol_exp(start, end, fib):
    exp = []
    # for every value in the range that satisfies the condition, added to a list named exp
    for i in range(start, end + 1):
        if fib % i == 0:
            exp.append(i)
    return exp

def loop_guarded_command(x, y, z, expressions):
    # choose a random expression and perform fibonacci calculation 
    chosen = random.choice(expressions)
    print("-----------")
    print(f"{z} % {chosen} == 0 is chosen")
    fibonacci(chosen)

def fibonacci(a):
    i, j = 0, 1
    print(f"{i} {j}", end="")
    temp = i + j

    while temp <= a:
        print(f" {temp}", end="")
        i, j = j, temp
        temp = i + j

try:
    input_numbers()
except RuntimeError as e:
    print("Error:", e)