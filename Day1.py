arr = [0,1,2,1,0]
n = len(arr)
if(n == 0):
    print("[]")

for i in range(1,n):
    key = arr[i]
    j = i-1
    while(j >= 0 and arr[j] > key):
        if(key < arr[j]):
            arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
            
for I in range(n):
    print(arr[I],end =" ")
