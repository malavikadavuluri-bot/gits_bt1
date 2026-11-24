item= "fried rice"
price =40
rating=4.5
is_veg=True
print(type(price))
print(type(item))
print(type(rating))
print(type(is_veg))

menu =["Dosa","Samosa","Idly"]
print(type(menu))

print(menu[2])
print(menu[0])
menu.append("vada")
menu[2] = "Puri"
menu[1]="Egg puff "
print(menu)
menu.remove("Dosa")
print(menu)

#print(price)
#print(item,"cost =",price)
#print(item)

working_days = ("Monday","Tuesday","Wednesday","Thursday","Friday")
#working_days[0] ="Sunday"
print(working_days[2])

prices = {
    "Dosa":40,
    "Idly":30,
     "Idly":30,
    "Samosa":15
}
#prices["Vada"] = 25
#prices["Idly"] = 35
#prices.pop("Samosa") 
print(prices)

#print(prices["Dosa"])
#print(prices["Idly"])
