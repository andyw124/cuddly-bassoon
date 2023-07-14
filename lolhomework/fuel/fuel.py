import fractions


def fuelcell():
    amount=input("Fraction: ")
    try:
        amount=fractions.Fraction(amount)
    except:
        fuelcell()
    else:
        if(float(amount)<=0.01):
            print("E")
        elif(float(amount)>1):
            fuelcell()
        elif(float(amount)>=0.99):
            print("F")
        else:
            print(str(round(float(amount)*100))+"%")

fuelcell()