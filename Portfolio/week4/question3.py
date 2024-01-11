# 3.Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur

# In[5]:


user_name = input("Hello, what is your name? ")
formatted_name = user_name.capitalize()
print(f"Hello, {formatted_name}. Good to meet you!")
