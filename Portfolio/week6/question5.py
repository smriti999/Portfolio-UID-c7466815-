
# 5. Another way to hide a message is to include the letters that make it up within
# seemingly random text. The letters of the message might be every fifth character,
# for example. Write and test a function that does such encryption. It should
# randomly generate an interval (between 2 and 20), space the message out
# accordingly, and should fill the gaps with random letters. The function should
# return the encrypted message and the interval used.
# For example, if the message is "send cheese", the random interval is 2, and for
# clarity the random letters are not random:
# send cheese
# s e n d c h e e s e
# sxyexynxydxy cxyhxyexyexysxye
# 

# In[5]:


import random
import string

def random_encrypt(message):
    interval = random.randint(2, 20)
    random_letters = string.ascii_letters
    encrypted_message = ""

    for i, char in enumerate(message):
        if char.isalpha():
            encrypted_message += char
        else:
            encrypted_message += random.choice(random_letters)

        if (i + 1) % interval == 0:
            encrypted_message += random.choice(random_letters)

    return encrypted_message, interval
message_to_encrypt = input("Enter a message to encrypt: ")
encrypted_message, interval_used = random_encrypt(message_to_encrypt)
print(f"Random Encryption: {encrypted_message} (Interval: {interval_used})")