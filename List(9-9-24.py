'''a=[10,20,30,40,50]'''
'''print(a[-3])
print(a[3])'''
'''for i in a:
    print(i)'''




'''using list()function to create list''' 
'''a=list(x*2 for x in range(1,10))
print(a)'''




customer=["sk","elavaransan","ram","lokesh","rr"]
amount=[2000,4000,6000,80000,10000]


s=input("enter sender Name:")
r=input("enter receiver Name:")
sendamt=int(input("Amount:"))



for i in customer:
    if(i==s):
        print("sender is available")
        b=(customer.index(i))
        print("The sender balance",amount[b])
        print("the sender current balance:",amount[b]-sendamt)
        print("sender debited amount",sendamt)
        break
    if(i==r):
        print("receiver name:",r)
        z=(customer.index(i))
        print("the receiver balance:",amount[z])
        print("the receiver current balance:",amount[z]+sendamt)
        break
   
    
           
               


'''for i in range(1,10,1):
    if(i==5):
        break
    print(i)'''

'''for i in range(1,10,1):
    if(i==5):
        continue
    print(i)'''

'''for i in range(1,10,1):
    if(i==5):
        pass
    print(i)'''



'''a=(100)
print("a")'''


'''a=input("enter a number:")
print("mama")'''

         

