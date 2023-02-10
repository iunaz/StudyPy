"""1"""
# def div(x,y):
#     return x/y
#
# x = int(input("x = "))
# y = int(input("y = "))
#
# try:
#     print(div(x,y))
# except ZeroDivisionError:
#     print("Не дели на ноль!")

"""2"""

# def PersonalInformation(surname, name, data, city, email, phone):
#     print(surname, name, data, city, email, phone)
#
# PersonalInformation(surname ="Ivanov", name = "Kiril", data = "07.11.1995", city = "Brest", email = "finni@mail.ru", phone = "+7(985)3671568")

"""3"""
# def my_func(x, y, z):
#     mylist = [x, y, z]
#     mylist = sorted(mylist)
#     return mylist[1] + mylist[2]
#
# print(my_func(13,9,12))

"""4"""

# def my_func(x,y):
#     for i in range(y-1):
#         x*=x
#     return x
# x = int(input("x = "))
# y = int(input("y = "))
# print(my_func(x,y))

"""5"""
#
# print("Для завершения введите * \n")
# flag = 0
# n = 0
# while flag == 0:
#     mylist = list(input().split())
#     res = 0
#     for i in range(len(mylist)):
#         if mylist[i] == "*":
#             flag = 1
#             break
#         else:
#             res += int(mylist[i])
#     n += res
#     print(n)

"""6"""
#
# def int_func(text):
#     for i in range(len(text)):
#         text[i] = text[i].title()
#     return text
#
# text = input("Введите текст ").split()
# print(" ".join(int_func(text)))
#
#









