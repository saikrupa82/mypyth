s=eval(input("Enter any number"))
for i in range(1,s):
    if i%3==0 and i%5==0:
        print(i,"fizz buzz")
    elif i%3==0:
        print(i,"fizz")
    elif i%5==0:
        print(i,"buzz")
  
    else:
        print(i)
        
