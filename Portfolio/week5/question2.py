# 2. Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument).
# 

# In[11]:


import shutil

def create_backup(file_path):
    try:
        shutil.copy2(file_path, file_path + ".bak")
        print(f"Backup created successfully: {file_path}.bak")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")

if __name__ == "__main__":
    file_path = input("Enter the name of the file to create a backup: ")
    create_backup(file_path)