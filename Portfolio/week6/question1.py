# 1. Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

# In[1]:


def to_binary_representation(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary
positive_integer = int(input("Enter a positive integer: "))
binary_representation = to_binary_representation(positive_integer)
print(f"Binary representation of {positive_integer}: {binary_representation}")
