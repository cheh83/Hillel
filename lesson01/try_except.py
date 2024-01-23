try:
    num = int(input("введите число: "))
    num += 5
    print(num)
except ValueError:
    print("вы ввели что-то не то")
