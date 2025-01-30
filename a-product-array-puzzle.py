array=[100,9,40]
selected=100
multiplication_value =1
def multiply(multiplication_value, i):
    return multiplication_value*i
for i in array:
    if(i!=selected):
        multiplication_value = multiply(multiplication_value, i)
print(multiplication_value)