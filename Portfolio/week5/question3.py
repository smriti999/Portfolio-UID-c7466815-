# 3. Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.

# In[1]:


import sys

def find_shortest_argument():
    arguments = []

    while True:
        user_input = input("Enter a command-line argument (press Enter to finish): ")
        
        if user_input == "":
            break

        arguments.append(user_input)

    if arguments:
        shortest_argument = min(arguments, key=len)
        print(f"The shortest command-line argument is: {shortest_argument}")
    else:
        print("No command-line arguments provided.")

if __name__ == "__main__":
    find_shortest_argument()