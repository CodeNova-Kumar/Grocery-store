def displaymenu():
    print("We have the following products at our store: ")
    dict={1:"Ice Cream",2:"FRUIT",3:"OIL",4:"JUICE"}
    for i in range (1,5):
        print(i,dict.get(i))
    choice=input("Please Enter the serial number or name of product ")
    choice=choice.upper()
    if choice=="1" or choice=="2" or choice=="3" or choice=="4":
        sno=int(choice)
        choice=dict.get(sno)
        return choice
    else:
        return choice


def brands(choice):

    print("We have the following", choice,"brands")
    if choice=="Ice Cream":
        items = {1: "STRAWBERRY", 2: "CARAMEL", 3: "NESTEL",4:"CHOCOALTE"}
        mrp = {"STRAWBERRY": 10,"CARAMEL": 20,"NESTEL": 15,"CHOCOALTE":10}
    if choice=="FRUIT":
        items = {1: "APPLE", 2: "BANANA", 3: "ORANGE", 4: "GRAPES"}
        mrp = {"APPLE": 120, "BANANA": 120, " ORANGE": 135,"GRAPES": 130, }
    if choice=="OIL":
        items = {1: "DHARA", 2: "FORTUNE", 3: "SAFFOLA", 4: "PATANJALI"}
        mrp = {"DHARA": 100,  "FORTUNE": 120,"SAFFOLA": 150, "PATANJALI": 110}
    if choice=="JUICE":
        items = {1: "TROPICANA", 2: "REAL", 3: "FRESH", 4: "NESTLE"}
        mrp = {"TROPICANA": 20,  "REAL": 20,  "FRESH": 15,  "NESTLE": 10}
    for i in range(1, 5):
         item=items.get(i)
         price=mrp.get(item)
         print(i, item, "Rs.", price)
    brand=input("Enter the serial number or name of brand ")
    brand= brand.upper()
    if brand == "1" or brand == "2" or brand == "3" or brand == "4":
        sno = int(brand)
        brand = items.get(sno)
        return brand
    else:
        return brand

def noofitem(brand,product):
    print("Enter the number of",brand,product,"you want ")
    quantity=int(input())
    return quantity

def price(brand,quantity):
    mrp = {"": 10, "CARAMEL": 20, "NESTEL": 15, "CHOCOALTE": 10,
           "APPLE": 120, "BANANA": 120, "ORANGE": 135,"ORANGE": 130,
           "DHARA": 100, "FORTUNE": 120, "SAFFOLA": 150, "PATANJALI OIL ": 110,
           "TROPICANA": 20, "REAL": 20, "FRESH": 15, "NESTLE": 10}
    price=mrp.get(brand)*quantity
    return price

product=[]
company=[]
quantity=[]
total=[]
answer="YES"
def new_func(brands, choice):
    brand=brands(choice) #returns the brand of product
    return brand

if __name__=="__main__":
        print("Welcome")
        user=input("What is your good Name Dear ")
        print("Hi",user,",We are glad to welcome you to our shop")
        while answer == "YES":
            choice=displaymenu() #returns the product

            product.append(choice)   #inserts the product into a list
            brand = new_func(brands, choice)
            company.append(brand)   #inserts the brand into a list

            amount=noofitem(brand,choice) #returns the number of product
            quantity.append(amount)     #inserts the number of products into a list
            prices=price(brand,amount) #returns the price of the product times the number
            total.append(prices)     #inserts the total into a list
            answer=input("Would you like to continue your shopping? Y(yes)/N(no)")
            answer=answer.upper()
            if answer!="YES":
                if answer=="Y":
                    answer="YES"
                if answer=="N":
                    answer=="NO"
                else:
                    answer=="NO"
            for z in range(0,len(product)):
                print(z+1,"Product:",product[z],"Brand:",company[z],"Quantity:",quantity[z],"Total price:",total[z])
            print(user,"Your total payable amount is: Rs",sum(total)),