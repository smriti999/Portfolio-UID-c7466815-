# 8.Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.

# In[10]:


temperatures = []

while True:
    user_input = input("Enter temperature in Centigrade (press Enter to finish): ")
    
    if user_input == "":
        break
    
    try:
        temperature = float(user_input)
        temperatures.append(temperature)
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

if temperatures:
    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    mean_temperature = sum(temperatures) / len(temperatures)

    print(f"Maximum temperature: {max_temperature:.2f}C")
    print(f"Minimum temperature: {min_temperature:.2f}C")
    print(f"Mean temperature: {mean_temperature:.2f}C")
else:
    print("No temperatures entered.")

