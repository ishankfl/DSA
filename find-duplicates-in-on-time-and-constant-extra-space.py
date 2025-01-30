array = [1,9,9,22,22,3,44,55,6,7,7]
new_array=[]
for i in range(len(array)):
    # dont do code
    for j in range(i):
        
        if(array[i]==array[j]):
            new_array.append(array[i])
print(new_array)