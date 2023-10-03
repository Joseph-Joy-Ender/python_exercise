price = int(input("Enter price: "))
name_of_item = str(input("Enter name of the item: "))
credit_score_status = str(input("Enter credit score status(enter true for good credit score and "
                                "false for bad credit score:"))


def print_header():
    print("***************************************")
    print("       Invoice                         ")
    print("***************************************")


def print_content(name_Of_Item, discounts, deposits):
    print("Name of item: ", name_of_item)
    print("Discount: ", discounts) 
    print("Deposit: ", deposits)


if credit_score_status == "true":
    print_header()
    discount = (price * 10)/100
    deposit = (price * 10)/100
    print_content(name_of_item, discount, deposit)
else:
    print_header()
    deposit = (price * 25)/100
    discount = 0
    print_content(name_of_item, discount, deposit)




