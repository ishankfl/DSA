a = [1,2,3,-4,-5]
target = -9

def rangefunction(a,target):
 for i in range(0,len(a)-1):
    for j in range(i, len(a)):
        if a[j] + a[i] == target:
            return [[a[j], a[i]],target]
 return 0;      
print(rangefunction(a,target))