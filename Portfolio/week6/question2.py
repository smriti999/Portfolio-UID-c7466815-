# 2. Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).
# 

# In[2]:


def get_factors(integer):
    factors = []
    for i in range(1, integer + 1):
        if integer % i == 0:
            factors.append(i)
    return factors
number = int(input("Enter an integer: "))
factors = get_factors(number)
print(f"Factors of {number}: {factors}")
