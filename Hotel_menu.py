menu={
    "pizza":99,
   "manchuria":60,
    "burger":40,
    "past":75,
    "coke":30,
    "noodles":60
}
print ("pizza:99\nmanchuria:60\nburger:40\npast:75\ncoke:30\nnoodles:60")

bill=0
item_1=input("Enter the item what do you want: ")
if item_1 in menu:
    bill+=menu[item_1]
    print(f"Your  item {item_1}  has been added to your order.")
else:
    print(f"Your ordered item {item_1}  not avaliable right now.")


another= input("Do you want another item (yes/no): ")
if another =="yes":
    item_2=input("Enter the item what do you want: ")
    if item_2 in menu:
         bill+=menu[item_2]
         print(f"Your  another item {item_2}  has been added to your order.")
    else: print(f"Your ordered item {item_2}  not avaliable right now.")
print(f"Your bill is {bill} rupees only.")    

       