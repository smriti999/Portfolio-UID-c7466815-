# 3. Write a program that manages a list of countries and their capital cities. It should
# prompt the user to enter the name of a country. If the program already "knows"
# the name of the capital city, it should display it. Otherwise it should ask the user to
# enter it. This should carry on until the user terminates the program (how this
# happens is up to you).
# Note: A good solution to this task will be able to cope with the country being entered
# variously as, for example, "Wales", "wales", "WALES" and so on.

# In[ ]:


country_capitals = {}

def get_capital(country):
    return country_capitals.get(country.lower())

def add_or_update_country(country, capital):
    country_capitals[country.lower()] = capital

def main():
    while True:
        user_input = input("Enter the name of a country (or 'exit' to terminate): ").strip()

        if user_input.lower() == 'exit':
            break

        capital = get_capital(user_input)
        if capital:
            print(f"The capital of {user_input} is {capital}.")
        else:
            new_capital = input(f"We don't know the capital of {user_input}. Enter it: ").strip()
            add_or_update_country(user_input, new_capital)
            print(f"Added {user_input} with the capital {new_capital} to the list.")

if __name__ == "__main__":
    main()