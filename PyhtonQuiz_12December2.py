# Ask the user to input a list
user_input = input("Enter a list of elements: ")

# Convert the input string into a list
user_list = user_input.split()

# Print the original list
print("Original list:", user_list)

# Print the reversed list
print("Reversed list:", user_list[::-1])

