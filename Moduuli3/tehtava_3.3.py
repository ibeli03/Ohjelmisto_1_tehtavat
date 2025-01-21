gender=input("Enter your gender: ")
hemoglobin=float(input("Enter your hemoglobin values (g/l): "))

if gender=="Male":
    if hemoglobin <=134 and hemoglobin >=167:
        print("Hemoglobin is normal")
    elif hemoglobin <134:
        print("Hemoglobin is too low")
    elif hemoglobin >167:
        print("Hemoglobin is too high")
if gender=="Female":
    if hemoglobin <=117 and hemoglobin >=155:
        print("Hemoglobin is normal")
    elif hemoglobin <117:
        print("Hemoglobin is too low")
    elif hemoglobin >155:
        print("Hemoglobin is too high")




