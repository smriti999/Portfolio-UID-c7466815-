# 1.Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.

# In[1]:


name = input("Hello, what is your name? ")

if name:
    print(f"Hello, {name}. Good to meet you!")
else:
    print("Hello, Stranger!")