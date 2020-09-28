import time
import bst_node_class

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# The idea is to put all of the names in the first list into an alphabetized binary tree.
# Once that tree is created, look through the array of names in the second list and 
# compare each one to the existing tree.
# If the tree contains that name, add it to the duplicates list.
name1_tree = bst_node_class.BSTNode(names_1[0])
for name_1 in names_1[1:]:
    name1_tree.insert(name_1)

for name_2 in names_2:
    if name1_tree.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time2 = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates2 = []

duplicates2 = set(names_1).intersection(names_2)

end_time2 = time.time()
print (f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
print (f"runtime: {end_time2 - start_time2} seconds")