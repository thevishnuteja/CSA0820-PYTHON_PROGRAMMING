def happy(num):  
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=digit**2+sum
        temp=temp//10
    return sum  
        
print("List of happy numbers between 1 and 100: ");  
for i in range(1, 101):  
    result = i;
    
    while(result != 1 and result != 4):  
        result = happy(result);  
      
    if(result == 1):  
        print(i,end =" ")  
       # print(" "),  
