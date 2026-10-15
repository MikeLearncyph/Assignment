sex = input("please enter your gender female/male: ")
hemoglobin = float(input("please enter your hemoglobin: "))
if sex == "female":
    if hemoglobin < 117:
        print ("your hemoglobin is low")
    elif 117 <= hemoglobin <= 155:
        print ("your hemoglobin is normal")
    else:
        print ("your hemoglobin is high")

if sex == "male":
    if hemoglobin < 134:
        print ("your hemoglobin is low")
    elif 134 <= hemoglobin <= 167:
        print ("your hemoglobin is normal")
    else:
        print ("your hemoglobin is high")




