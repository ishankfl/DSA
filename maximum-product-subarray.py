array= [2,-4,-5,100]
subarry=[]
for i  in range (len(array)):
    
    for j in range(i,len(array)):
        subarry.append(array[i:j+1])
    # print(subarry)
max_value=0 
print(subarry)
for each in subarry:
    multiplication=1
    for i in each:
        multiplication = i*multiplication
    if(multiplication>max_value):
        max_value=multiplication
print(max_value)