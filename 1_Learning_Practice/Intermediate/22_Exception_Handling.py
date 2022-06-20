# Types of Errors

# 1. Compile Time Errors  --> Syntax Errors
# 2. Logical Errors       --> Logical Mistake Where the code will Execute and gives the Output
#                             But Does not Give the exact Output Required.
# 3. Runtime Errors       --> The Moment we get A Runtime Error the Execution of the Program Will Stop

a = 5
b = 0

try:
    print("Resource Open")
    print(a / b)
except Exception as e:
    print("Error - ", e)
else:
    print("No Exception")
finally:
    print("Resource Closed")


