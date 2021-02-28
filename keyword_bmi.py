def calc_bmi(weight,height):
    return weight / (height / 100) ** 2

bmi1 = calc_bmi(weight = 73,height = 167)
print("bmi1=" + str(bmi1))

bmi2 = calc_bmi(height = 167,weight = 73)
print("bmi2=" + str(bmi2))
