N = int(input("enter a number: "))

for i in range(N):
    for j in range(0, i + 1):
        print("*", end = "") 
    print() 

	
for i in range(1, N):
    for j in range(i, N):
        print("*", end = "") 
    print() 



