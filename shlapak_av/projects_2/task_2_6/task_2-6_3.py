phenotype_patient= int(input("Введите фенотип группы крови пациента (1, 2, 3, 4): "))
phenotype_recipient= int(input("Введите фенотип группы крови реципента (1, 2, 3, 4): "))
if phenotype_patient == phenotype_recipient: 
    print("Переливание возможно")
elif phenotype_patient == 4 and phenotype_recipient == 1 or phenotype_recipient == 2 or phenotype_recipient == 3:
    print("Переливание возможно")
elif phenotype_patient == 2 or phenotype_patient == 3 and phenotype_recipient == 1:
    print("Переливание возможно")
else :
    print("Переливание невозможно")