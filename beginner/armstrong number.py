nm = int(input("Enter a number: "))  
sm = 0  
temp = nm  
  
while temp > 0:  
   digit = temp % 10  
   sm += digit ** 3  
   temp //= 10  
  
if nm == sm:  
   print(nm,"is an Armstrong number")  
else:  
   print(nm,"is not an Armstrong number") 
