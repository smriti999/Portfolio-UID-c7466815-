# 2.Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.
# 

# In[4]:


def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count
user_string = input("Enter a string: ")
result = count_upper_lower(user_string)
print("Uppercase letters:", result[0])
print("Lowercase letters:", result[1])