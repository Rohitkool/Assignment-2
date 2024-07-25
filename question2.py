# To print the number in the array by users input
array = []


num = int(input("How many elements would you like to add to the array? "))


for i in range(num):
    
    element = input(f"Enter element {i + 1}: ")
    
    array.append(element)

# Print the final array
print("Final array:", array)
