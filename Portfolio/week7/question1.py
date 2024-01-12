# 1. Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].

# In[ ]:


def unique_letters_sorted(string):
    unique_letters = sorted(set(char.lower() for char in string if char.isalpha()))
    return unique_letters
input_string = input("Enter a string: ")
result = unique_letters_sorted(input_string)
print(f"Sorted List of Unique Letters: {result}")