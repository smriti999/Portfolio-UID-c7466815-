# 6. Write a program that decrypts messages encoded as above.

# In[6]:


def decrypt_encrypted_message(encrypted_message, interval_used):
    decrypted_message = ""
    for i in range(0, len(encrypted_message), interval_used + 1):
        decrypted_message += encrypted_message[i]

    return decrypted_message
encrypted_message = input("Enter the encrypted message: ")
interval_used = int(input("Enter the interval used for encryption: "))
decrypted_message = decrypt_encrypted_message(encrypted_message, interval_used)
print(f"Decrypted Message: {decrypted_message}")