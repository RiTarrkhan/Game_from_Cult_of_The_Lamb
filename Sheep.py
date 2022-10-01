from random import randint as rand

a = [[], [], []]
b = [[], [], []]
rand_num = 0
nummy = 0


def sum_list(nummy):
    total = 0
    for nums in nummy:
        if len(nums) == 0:
            total += 0
        elif len(nums) == 1:
            total += nums[0]
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                total += nums[1] ** 2
            elif nums[0] != nums[1]:
                total += nums[0] + nums[1]
        elif len(nums) == 3:
            if nums[0] == nums[1] and nums[1] != nums[2]:
                total += nums[1] ** 2 + nums[2]
            elif nums[1] == nums[2] and nums[0] != nums[2]:
                total += nums[1] ** 2 + nums[0]
            elif nums[0] != nums[1] and nums[1] != nums[2]:
                total += nums[0] + nums[1] + nums[2]
            elif nums[0] == nums[2] and nums[1] != nums[2]:
                total += nums[2] ** 2 + nums[1]
            elif nums[0] == nums[1] == nums[2]:
                total += nums[2] ** 3
    return total
C:\Users\ritar\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\scratch.py

def choise(rand_num, nummy, label):
    if rand_num in nummy[0] and label == 1:
        nummy[0].remove(rand_num)
    elif rand_num in nummy[1] and label == 2:
        nummy[1].remove(rand_num)
    elif rand_num in nummy[2] and label == 3:
        nummy[2].remove(rand_num)
    return nummy


def choise_row(nummy, rand_num):
    rowy = input("Выберите ряд")
    count = 0
    flag = 1
    while count == 0:
        if int(rowy) == 0:
            flag = 0
            count += 1
            return 0
        elif rowy.isdigit() is False:
            rowy = input("Выберите число")
        elif int(rowy) < 0 or int(rowy) > 3:
            rowy = input("Выберите число от 0 до 3")
        elif 0 < int(rowy) <= 3:
            if len(nummy[int(rowy) - 1]) == 3:
                rowy = input("Выберите другой ряд")
            else:
                nummy[int(rowy) - 1].append(rand_num)
                count += 1
                label = int(rowy)
                return label


name_1 = str(input("Как вас зовут?"))
name_2 = str(input("Как вас зовут?"))
d_x = str(input("Сколько граней у кости?"))
result_1 = None
result_2 = None
while not ((len(a[0]) == len(a[1]) == len(a[2]) == 3 or len(b[0]) == len(b[1]) == len(b[2]) == 3)):
    print("%(name_1)s" % {"name_1": name_1})
    rand_num = rand(1, int(d_x))
    print("Вам выпало", rand_num)
    print("Поля", a, b, sep="\n")
    player_1 = sum_list(a)
    player_2 = sum_list(b)
    print("Счет", player_1, player_2, sep="\n")
    result_1 = choise_row(a, rand_num)
    if result_1 == 0:
        break
    print(a, choise(rand_num, b, result_1))
    print("%(name_2)s" % {"name_2": name_2})
    rand_num = rand(1, int(d_x))
    print("Вам выпало", rand_num)
    print("Поля", a, b, sep="\n")
    count = 0
    player_1 = sum_list(a)
    player_2 = sum_list(b)
    print("Счет", player_1, player_2, sep="\n")
    result_2 = choise_row(b, rand_num)
    if result_2 == 0:
        break
    print(choise(rand_num, a, result_2), b)


player_1 = sum_list(a)
player_2 = sum_list(b)
print("Счет", player_1, player_2, sep="\n")

if result_1 == 0:
    print("%(name_1)s сдался" % {"name_1": name_1})
elif result_2 == 0:
    print("%(name_2)s сдался" % {"name_2": name_2})
elif player_1 > player_2:
    print("%(name_1)s выиграл" % {"name_1": name_1})
elif player_1 < player_2:
    print("%(name_2)s выиграл" % {"name_2": name_2})
elif player_1 == player_2:
    print("Ничья")

