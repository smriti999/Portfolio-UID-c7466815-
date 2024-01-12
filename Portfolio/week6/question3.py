# 3. Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.
# 

# In[3]:


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
integer = int(input("Enter an integer: "))
if is_prime(integer):
    print(f"{integer} is a prime number.")
else:
    print(f"{integer} is not a prime number.")


