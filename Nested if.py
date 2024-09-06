a=int(input("enter first value:"))
b=int(input("enter second value:"))
c=int(input("enter third value:"))
if(a>b):
    if(a>c):
        print("A")
    else:
        print("C")
else:
    if(b>c):
        print("B")
    else:
        print("C")





a=int(input("enter first value:"))
b=int(input("enter second value:"))
c=int(input("enter third value:"))
d=int(input("enter fourth value:"))
if(a>b):
    if(a>c):
        if(a>d):
            print("A")
        else:
            print("D")
    else:
         print("C")
else:
    if(b>c):
        if(d>c):
            if(b>d):
                print("B")
            else:
                print("D")
        else:
            print("C")
    else:
        print("C")
       
              
        
