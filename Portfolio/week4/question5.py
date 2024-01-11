# 5.Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).

# In[7]:


def celsius_to_fahrenheit(celsius): return celsius * 9/5 + 32
def fahrenheit_to_celsius(fahrenheit): return (fahrenheit - 32) * 5/9
celsius_temperature = float(input("Enter temperature in Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is {fahrenheit_temperature:.2f} Fahrenheit.")

fahrenheit_temperature_input = float(input("Enter temperature in Fahrenheit: "))
celsius_temperature_output = fahrenheit_to_celsius(fahrenheit_temperature_input)
print(f"{fahrenheit_temperature_input} Fahrenheit is {celsius_temperature_output:.2f} Celsius.")