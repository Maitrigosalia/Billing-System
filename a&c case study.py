#A&C clothing company case study

u=input("Enter user =")
p=input("Enter ps =")
d=0
if (u=="ac") and (p=="store"):
    print("Enter credentials")
    Date= (input("DD/MM/YYYY:"))
    Day= input("Enter Day :")
    Name= input("Full Name of the customer :")
    Bill= eval(input("Enter Bill Amount :"))
    if (Bill > 1000)& (Bill < 2000):
        d= 0.10 * Bill
    elif (Bill > 2000) & (Bill < 3000):
        d= 0.20 * Bill
    elif (Bill > 3000) & (Bill < 4000):
        d= 0.30 * Bill
    elif (Bill > 4000):
        d= 0.40 * Bill
    Do_you_have_a_coupon_to_avail_dicount = input("Do you have a coupon to avail dicount (YES/NO)?")   
    if Do_you_have_a_coupon_to_avail_dicount== 'YES':
        amt= Bill - 90
        TB= amt - d
        print("Your Bill amount after using coupon",TB)
    else:
        print("IF YOU ARE PURCHASING A COUPON CODE THEN IT WILL BE AVAILED FROM YOUR NEXT PURCHASE ONLY AND THAT THEY HAVE TO AVAIL IT BEFORE 40 DAYS OF BUYING THE COUPON")

        Do_you_want_to_buy_coupon_code_=input("Do you want to buy coupon code (YES/NO) ?")
        if Do_you_want_to_buy_coupon_code_=='YES':
            amt = 90 + Bill
            TB = amt - d
            print("Your Bill amount after buying 90 ruppee coupon",TB)
        else:
            TB= Bill - d 
            print("Your bill amount without coupon:", TB)
            
    print("TOTAL BILL")
    print("Date :", Date)
    print("Day  :", Day)
    print("Name :", Name)
    print("Bill :", Bill)
    print("Disc :", d)
    print("TB   :", TB)
    print("Thank you visit again")
else:
    print("Enter correct credentials")
            
            
            
        
      
        



        

    

                
                
                
                
            

