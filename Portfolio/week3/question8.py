# 8.Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times".

# In[9]:


table_number = int(input("Enter the number for the times table: "))

if table_number < 0:
    for i in range(12, -1, -1):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
elif 0 <= table_number <= 12:
    for i in range(13):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
else:
    print("Error: Please enter a number between -12 and 12.")