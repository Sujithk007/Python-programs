num =int(input())
if num > 1: 
   for i in range(2, num//2): 
       if (num % i) == 0: 
           print( "no") 
           break
   else: 
       print("yes") 
else: 
   print("no") 
