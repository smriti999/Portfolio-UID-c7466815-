# 5. Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided!

# In[4]:


def process_temperature_readings():
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
        print("No valid temperature readings provided.")

if __name__ == "__main__":
    process_temperature_readings()
