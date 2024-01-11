# 6. Write a program that takes the name of a file as a command-line argument, and
# creates a backup copy of that file. The backup should contain an exact copy of the
# contents of the original and should, obviously, have a different name.
# Hint: By now, you should be getting the idea that there is a built-in way to do the
# heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.

# In[ ]:


import shutil

def create_backup():
    file_path = input("Enter the name of the file to create a backup: ")
    try:
        shutil.copy2(file_path, file_path + ".bak")
        print(f"Backup created successfully: {file_path}.bak")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")

if __name__ == "__main__":
    create_backup()

