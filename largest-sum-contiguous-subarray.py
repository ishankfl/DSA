array = [-5, -6, -1000, -90, 200, 300]
final_array = []

# Generating all possible subarrays
for i in range(len(array)):
    for j in range(i, len(array)):
        print(array[i:j+1])
        final_array.append(array[i:j+1])  # Include all subarrays

print("Final array:", final_array)

# Dictionary to store sum of each subarray
dic = {i+1: sum(each) for i, each in enumerate(final_array)}
print(dic)
# Finding max value
max_value = max(dic.values())  # This will give 500
print("Max value:", max_value)
