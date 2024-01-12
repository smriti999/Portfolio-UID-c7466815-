# 2. Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.
# Hint: These could all be done programmatically, but consider carefully what topic we
# have been discussing this week! Each function can be exactly one line.

# In[ ]:

def unique_letters_sorted(string):
    unique_letters = sorted(set(char.lower() for char in string if char.isalpha()))
    return unique_letters

def letters_in_either(word1, word2):
    return unique_letters_sorted(word1 + word2)

def letters_in_both(word1, word2):
    return unique_letters_sorted(set(word1) & set(word2))

def letters_in_either_not_both(word1, word2):
    return unique_letters_sorted((set(word1) | set(word2)) - (set(word1) & set(word2)))
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

result_either = letters_in_either(word1, word2)
result_both = letters_in_both(word1, word2)
result_either_not_both = letters_in_either_not_both(word1, word2)

print(f"Letters in either word: {result_either}")
print(f"Letters in both words: {result_both}")
print(f"Letters in either, but not both: {result_either_not_both}")