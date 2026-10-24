print("=====Electricity bill calculator=====")
units=int(input("enter your units:"))
if units>=0 and units<=100:
    print("rate 10 per units")
    bill=units*10
    print("your total bill is",bill)
elif units>100 and units<=200:
    print("rate is 15 per units")
    bill=units*15
    print("your total bill is",bill)
elif units>200 and units<=300:
    print("rate is 20 per units")
    bill=units*20
    print("your bill is",bill)
elif units>300:
    print("rate 25 per units")
    bill=units*25
    print("your total bill is",bill)
elif units<0:
    print("invalid units")
if bill>=5000:
    print("you bill is greater then 5000.now we add 5 percent tix services")
    tax=bill*0.05
    print("the amount of tax that we add is",tax)
    total_bail=bill+tax
    print("Now your final total bill is",total_bail)