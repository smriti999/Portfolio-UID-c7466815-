# 4.When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)
# 

# In[1]:


def remove_last_character(input_string):
    if len(input_string) <= 1:
        return input_string
    else:
        return input_string[:-1]

# Test the function
test_string_1 = "Hello"
test_string_2 = "A"
test_string_3 = ""

result_1 = remove_last_character(test_string_1)
result_2 = remove_last_character(test_string_2)
result_3 = remove_last_character(test_string_3)

result_1, result_2, result_3