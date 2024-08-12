info_1 = input(). split()
info_2 = input(). split()

age_1 = int(info_1[0])
sex_1 = info_1[1]
age_2 = int(info_2[0])
sex_2 = info_2[1]

if (age_1 >= 19 and sex_1 == 'M') or (age_2 >= 19 and sex_2 == 'M'):
    print(1)
else:
    print(0)