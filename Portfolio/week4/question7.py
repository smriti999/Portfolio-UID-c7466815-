# 7.Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean.
# 

# In[9]:


temperatures = []

while len(temperatures) < 6:
    try:
        temperature = float(input(f"Enter temperature {len(temperatures) + 1} in Centigrade: "))
        temperatures.append(temperature)
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

max_temperature = max(temperatures)
min_temperature = min(temperatures)
mean_temperature = sum(temperatures) / len(temperatures)

print(f"Maximum temperature: {max_temperature:.2f}C")
print(f"Minimum temperature: {min_temperature:.2f}C")
print(f"Mean temperature: {mean_temperature:.2f}C")