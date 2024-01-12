# 4. Computers are commonly used in encryption. A very simple form of encryption
# (more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
# containing a message and "encrypts" it in this way.
# 

# In[4]:


def simple_encrypt(message):
    message_without_spaces = message.replace(" ", "")
    encrypted_message = message_without_spaces[::-1]
    return encrypted_message
message_to_encrypt = input("Enter a message to encrypt: ")
encrypted_message = simple_encrypt(message_to_encrypt)
print(f"Simple Encryption: {encrypted_message}")