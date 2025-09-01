n = int(input("Enter a number: "))
count = 0
for j in range(1, n+1):
    if(n % j == 0):
        count += 1
        
print(f"Total factor of {n} is {count}")
