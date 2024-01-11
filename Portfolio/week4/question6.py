# 6.Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format

# In[8]:


user_input = input("Enter a temperature in Centigrade (e.g., 25C): ")
temperature, unit = float(user_input[:-1]), user_input[-1].upper()

if unit == 'C':
    fahrenheit_temperature = temperature * 9/5 + 32
    print(f"{user_input} is equivalent to {fahrenheit_temperature:.2f}F.")
else:
    print("Invalid input. Please enter a temperature in Centigrade with the format like '25C'.")
