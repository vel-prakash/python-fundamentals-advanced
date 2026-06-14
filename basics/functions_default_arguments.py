# Default arguments provide predefined values for parameters.
# The default value is used when an argument is omitted.
# They make functions more flexible and reduce the number of arguments
# that must be supplied when calling a function.
#
# Argument types:
# 1. Positional
# 2. Default
# 3. Keyword
# 4. Arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1, 0))


import time

# Default parameters must come after non-default parameters.
def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)

    print("DONE!")

count(30, 15)