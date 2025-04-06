
# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"The list after appending the is {my_list}.")

my_list.insert(1, 15)
print(f"The list after inserting 15 in position index 1 is {my_list}.")

my_list.extend([50, 60, 70])
print(f"The list after extenting is {my_list}.")

del my_list[-1]
print(f"The list after deleting the last item in the list is {my_list}.")

# Sort my_list in ascending order.
my_list.sort()
print(f"The sort result is {my_list}.")

index_30 = my_list.index(30)
print(f"The index of 30 is {index_30}")
print(f"Final result is {my_list}")
