# 4. Write a program that takes a URL as a command-line argument and reports
# whether or not there is a working website at that address.
# Hint: You need to get the HTTP response code.
# Another Hint: StackOverflow is your friend.

# In[3]:


import requests

def check_website_availability():
    url = input("Enter the URL to check: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website at {url} is accessible.")
        else:
            print(f"The website at {url} returned a non-OK status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Unable to connect to {url}. Please check the URL.")

if __name__ == "__main__":
    check_website_availability()


