# 4. One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the different symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.
# Write a program that processes a string representing a message and reports the six
# most common letters, along with the number of times they appear. Case should
# not matter, so "E" and "e" are considered the same.
# Hint: There are many ways to do this. It is obviously a dictionary, but we will want
# zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
# best to ignore that initially, and then check the usual resources for the runes

# In[ ]:


def frequency_analysis(message):
    frequency_dict = {}

    for char in message.lower():
        if char.isalpha():
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    sorted_frequencies = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    print("Six most common letters and their frequencies:")
    for i in range(min(6, len(sorted_frequencies))):
        print(f"{sorted_frequencies[i][0]}: {sorted_frequencies[i][1]}")

# Example Usage:
encrypted_message = input("Enter the encrypted message: ")
frequency_analysis(encrypted_message)