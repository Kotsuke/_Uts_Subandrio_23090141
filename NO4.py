bb = int(input("Masukan Berat Badan :"))
tb = int(input("Masukan Tinggi Badan : "))
BMI = bb/tb
print("Berat Badan :",bb)
print("Tinggi Badan :",tb)
print("Hasil BMI :",BMI)

if BMI > 15.5:
    print("Berat Badan Kurang")
elif 18.5<= BMI < 24.9:
    print("Berat Badan Normal")
elif 25 <=BMI < 29.9:
    print("Kelebihan Berat Badan")
elif BMI >=30 :
    print("Obesitas")