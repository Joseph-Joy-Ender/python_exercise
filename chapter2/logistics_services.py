def decide_parcel_amount(delivery_number: int):
    if 1 < delivery_number > 100:
        raise Exception("Amount must be between 1 and 100")

    if delivery_number < 50:
        return 160
    elif delivery_number <= 59:
        return 200
    elif delivery_number <= 69:
        return 250

    return 500
#
# num = int(input("number of delivery"))
# print(decide_parcel_amount(num))
