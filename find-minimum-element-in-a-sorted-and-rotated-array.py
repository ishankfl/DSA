
def findMin(array):
    res = array[0]
    for i in range(len(array)):
        res = min(res, array[i])
    return res

if __name__ == "__main__":
    print(findMin([1,2,3,4,5,6,2,3,-100]))