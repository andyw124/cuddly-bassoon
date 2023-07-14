me={
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
def reader(words):
    newp=""
    for i in words:
        newp+=i.lower()
    return newp
def foodmenu(menu,total=0.0,number=0):
    n=number
    try:
        ges=reader(input("Item: "))
    except EOFError:
        exit(0)
    else:
        try:
            total+=round(float(menu[ges]),2)
            print("Total: $"+str(total)+str(0))
        except:
            foodmenu(menu,total,n)
        else:
            if(ges=="super quesadilla"):
                pass
            elif(n==2):
                pass
            else:
                foodmenu(menu,total,n+1)
foodmenu(me)
