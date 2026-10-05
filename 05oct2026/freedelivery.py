


order_amount = float(input("enter order amount:"))
premium = input("do you have premium membership ?(yes/no):")
if order_amount >=1000 or premium =="yes":
    print("free delivery")
else:
    print("delivery charges apply")