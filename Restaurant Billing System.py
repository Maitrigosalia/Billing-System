#Exam(15/6/24)- GOOD VIBES FAST FOOD
print("************Hello and Welcome to Good Vibes Fast Food Restaurant********")
print("Where we serve food with good vibes :)")

print("Enter your choice")
print("1. View Menu")
print("2. Exit")

a=eval(input("Enter:"))
if a==1:
    print("Menu")
    print("S.no","Item", "Price")
    print(1, 'Pav bhaji', 80)
    print(2, 'Italian Pizza', 250)
    print(3, 'Arabiata Pizza', 200)
    print(4, 'Cheese Burger',40)
    print(5, 'Jain Burger', 35)
    print(6, 'French Fries', 75)
    print(7, 'Curly fries', 85)
    print(8, 'Thumbs up', 30)
    print(9, 'Coca Cola', 25)
    print(10,'Sprite', 25)

    c=eval(input("Enter your order:"))
    if c==1:
       print("Order Pav bhaji")
       Qnt=eval(input("Enter Quantity:"))
       p=80
    elif c==2:
        print("Order Italian Pizza")
        Qnt=eval(input("Enter Quantity:"))
        p=250
    elif c==3:
        print("Order Arabiata Pizza")
        Qnt=eval(input("Enter Quantity:"))
        p=200
    elif c==4:
        print("Order Cheese Burger")
        Qnt=eval(input("Enter Quantity:"))
        p=40
    elif c==5:
        print("Order Jain Burger")
        Qnt=eval(input("Enter Quantity:"))
        p=34
    elif c==6:
        print("Order French Fries")
        Qnt=eval(input("Enter Quantity:"))
        p=75
    elif c==7:
        print("Order Curly fries")
        Qnt=eval(input("Enter Quantity:"))
        p=85
    elif c==8:
        print("Order Thumbs up")
        Qnt=eval(input("Enter Quantity:"))
        p=30
    elif c==9:
        print("Order Coca cola")
        Qnt=eval(input("Enter Quantity:"))
        p=25
    elif c==10:
        print("Order Sprite")
        Qnt=eval(input("Enter Quantity:"))
        p=25

    Want_to_order_more_good_food= input("Want to order more food (YES/NO)?")
while True:
    if Want_to_order_more_good_food== 'YES':
        d=eval(input("Enter your order:"))
        p=0
        if d==1:
            print("Order Pav bhaji")
            Qnt=eval(input("Enter Quantity:"))
            p=80
        elif d==2:
            print("Order Italian Pizza")
            Qnt=eval(input("Enter Quantity:"))
            p=250
        elif d==3:
            print("Order Arabiata Pizza")
            Qnt=eval(input("Enter Quantity:"))
            p=200
        elif d==4:
            print("Order Cheese Burger")
            Qnt=eval(input("Enter Quantity:"))
            p=40
        elif d==5:
            print("Order Jain Burger")
            Qnt=eval(input("Enter Quantity:"))
            p=34
        elif d==6:
            print("Order French Fries")
            Qnt=eval(input("Enter Quantity:"))
            p=75
        elif d==7:
            print("Order Curly fries")
            Qnt=eval(input("Enter Quantity:"))
            p=85
        elif d==8:
            print("Order Thumbs up")
            Qnt=eval(input("Enter Quantity:"))
            p=30        
        elif d==9:
            print("Order Coca cola")
            Qnt=eval(input("Enter Quantity:"))
            p=25
        elif d==10:
            print("Order Sprite")
            Qnt=eval(input("Enter Quantity:"))
            p=25
            
    Want_to_order_more_good_food= input("Want to order more food (YES/NO) ?")
    if Want_to_order_more_good_food== 'NO':
        print("Calcuating Total Order")
        Amt=(p * Qnt)
        if Amt>301:
                d=0.02
                Tb=Amt-(Amt*d)+(Amt*0.05)
        elif Amt>=301 or Amt<=600:
                d=0.04
                Tb=Amt-(Amt*d)+(Amt*0.05)        
        elif Amt>601:
                d=0.08
                Tb=Amt-(Amt*d)+(Amt*0.05)
        print("Total Bill", Tb)
        break
                        
e=eval(input("Enter number to exit:"))         
if e==2:
    print("Exit")
    print("Thank you for Shopping with us")
    print("Have a great day :)")






