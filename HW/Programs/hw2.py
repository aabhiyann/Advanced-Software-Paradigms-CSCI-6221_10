import random #maybe need to do this


class TerminationException(Exception):
    pass


def input_numbers():
    while True:
        try:
            x, y, z = map(int, input("Enter three non-zero positive integers: ").split())

            if x <= 0 or y <= 0 or z <= 0 or x == y:
                print("Please provide three non-zero, positive integers (First two input can't be the same)")
                
            elif x>y:
                print("First input cannot be larger than second input")
                
            else:
                print(x, y, z)
                expressions = bol_exp(x, y, z)
                for exp in expressions:
                    print(exp)
                loop_guarded_command(x, y, z, expressions)
                break

        except ValueError as e:
            print(e)
            raise TerminationException()
            
def bol_exp(start, end, fib):
    exp = []
    for i in range(start, end + 1):
        if fib % i == 0:
            exp.append((f"{fib} % {i} == 0", i))
    if not exp:
        raise ValueError(f"{fib} is not divisible by numbers between {start} and {end} without a remainder. Program Terminated.")
    return exp

def loop_guarded_command(x, y, z, expressions):
    valid_expressions = [expr for expr, divisor in expressions if eval(expr)]
    
    if not valid_expressions:
        raise ValueError(f"{z} does not satisfy any expressions")
    chosen = random.choice(valid_expressions)
    chosen_exp, chosen_div = chosen
    print(f"{z} % {chosen_div} == 0 is chosen")
    fibonacci(chosen_div)

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
except TerminationException as e:
    print(e)