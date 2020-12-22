def bubble_sort(data):
    for num in range(len(data)):
        for j in range(len(data)- num - 1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data
data = [5,4,3,2,1,0,6,9,8]
print(bubble_sort(data))

def bubble_sort(data):
    for num in range(1,len(data)):
        for j in range(0,len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data
data = [-1,5,4,3,2,1,0,6,9,8,0,-10]
data1 = [5,4,3,2,1,0,6,9,8]
print(bubble_sort(data1))
