print ("The main purpose to make this program is to get familier with Python language and I really liked this project as a part of my curriculum because I learnt plenty of things while making this little bit Software. \n ")

print (" Welcome to AM's Shirt Cost Calculator \n")

print (" \n These are the available Colors we have. ")

print (" 1 == Black 4.3$ ")
print (" 2 == Blue  2.8$ ")
print (" 3 == white 8.5$ ")
print (" 4 == Yellow 3$ ")
print (" 5 == Orange 5.1$ ")

print (" \n What type of colour do you want to order? ")

num = int(input())

if num == 1:
    print (" You selected Black ")
    VOT = 4.3

elif num == 2: 
    print (" You selected Blue ")  
    VOT =2.8

elif num == 3:
    print (" You selected white ")   
    VOT =8.5

elif num == 4:
    print (" You selected Yellow ")
    VOT =3

elif num == 5:
    print (" You selected Orange ")    
    VOT =5.1

else: 
    print (" Please select 1 to 5 ")  

print (" 1 == Black Trouser 2.9$ ")
print (" 2 == Blue Trouser 5.4$ ")
print (" 3 == white Trouser 4.8$ ")         

vum = int(input())

if vum == 1:
    print (" You selected Black Trouser ")
    VOTS = 2.9

elif vum == 2: 
    print (" You selected Blue Trouser ")  
    VOTS =5.4

elif vum == 3:
    print (" You selected white Trouser ")   
    VOTS =4.8

else: 
    print (" Please select 1 to 3 ") 

type_of_shirt = int(input("\n enter 1 for a POLO and enter 2 for a T-shirt "))

if type_of_shirt == 1:
    print("\n You selected POLO ") 

elif type_of_shirt == 2:
    print(" You selected T-shirt")    

else:
    print (" Choose 1 or 2 ")

quantity = 2 
bill = float (VOT + VOTS)

print ("\n select your category from below options ")

print (" 1 == Student")
print (" 2 == Senior Citizen ")
print (" 3 == You are not eligible in this category ")

a=int(input("enter the category \n"))

if a==1 or a==2:
    print("nice you have 10% discount")
    if quantity>=3:
        print("15 % on that")
        no_hst=float(bill*0.25)


