def calc_fee(age,is_monday):
    fee = 2000
    if (age < 3):
        return 0
    elif (age < 6):
        fee = 500
    elif (age >= 60):
        fee = 1500
    if (is_monday):
        fee = fee - int(fee / 100 * 20)
    return fee
print (calc_fee(51,False))
print (calc_fee(51,True))


    
