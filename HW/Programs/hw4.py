# This program is written in Python

# class for Queue and it's functions
class Queue_adt:
    def __init__(self,datatype):
        self.datatype = datatype # datatype is checked in print_functions function for push operation
        self.queuearray = [] # use array to store queue data
        
    def push(self,data):
        self.queuearray += [data] # if push, add the new data to the existing array
        print(f" -- ({data}) has been pushed into the queue -- " )
        
    def pop(self):
        # if data exists in queue, remove the first data and let the user know
        if len(self.queuearray) > 0:
            data = self.queuearray[0]
            self.queuearray = self.queuearray[1:]
            print(f" -- ({data}) has been popped from the queue -- " )
        else:
            print(" -- There is no element left in the queue. So, nothing can be popped -- " )

    def count(self):
        print(f" -- The number of elements in the queue is : {len(self.queuearray)} --")
    
    
def input_type():
    print("Select an option:")
    print("a. Integer")
    print("b. String")
    
    # take one input from the user to determine the data type
    input_choice = input("Enter your choice: ").strip().lower()
    
    # checking which opetion the user selects
    if input_choice == 'a':
        integer_adt() #if user selects a, integer
    elif input_choice == 'b':
        string_adt() #if user selects b, string
    else:
        print("Invalid! (Please select a or b)")
        
def integer_adt():
    print("You've selected the Integer option.")
    integer_queue = Queue_adt(int)
    print_functions(integer_queue)

def string_adt():
    print("You've selected the String option.")
    string_queue = Queue_adt(str)
    print_functions(string_queue)
    
def print_functions(queue):
    while True:
        print("\n   -- Main Menu --   ")
        print("Select the desired function:")
        print("a. push")
        print("b. pop")
        print("c. count")
        print("d. end")
        input_choice = input("Enter the function to be used: ").strip().lower()
        
        if input_choice == 'a':
            if queue.datatype == int:
                try:
                    data = int(input("Enter the integer data to be pushed into the Queue: "))
                except ValueError:
                    print("Invalid input! Please enter an integer.")
                    continue
            elif queue.datatype == str:
                data = input("Enter the string data to be pushed into the Queue: ")
                
            queue.push(data) #if user selects a, push
        
        elif input_choice == 'b':
            queue.pop() #if user selects b, pop
            
        elif input_choice == 'c':
            queue.count() #if user selects c, count
            
        elif input_choice == 'd':
            print(" -- Program is ending...  -- ")
            break #if user selects d, terminate the program
        else:
            print("Invalid! (Please select a, b, c, or d)")
    
    
try:
    input_type() # function to take input type from the user (integer or string)
except RuntimeError as e:
    print("Error:", e)