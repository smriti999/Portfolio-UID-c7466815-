
# 5.The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group.

# In[1]:


students_1 = 113
students_2 = 175
students_3 = 12

students_per_group = 24

full_groups_1 = students_1 // students_per_group
remaining_students_1 = students_1 % students_per_group

full_groups_2 = students_2 // students_per_group
remaining_students_2 = students_2 % students_per_group

full_groups_3 = students_3 // students_per_group
remaining_students_3 = students_3 % students_per_group

print(f"For {students_1} students:")
print(f"   Full groups: {full_groups_1}")
print(f"   Remaining students: {remaining_students_1}\n")

print(f"For {students_2} students:")
print(f"   Full groups: {full_groups_2}")
print(f"   Remaining students: {remaining_students_2}\n")

print(f"For {students_3} students:")
print(f"   Full groups: {full_groups_3}")
print(f"   Remaining students: {remaining_students_3}")