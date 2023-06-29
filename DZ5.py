# def zad(a, b):
#     if a == b == 0:
#         return "Не имеет смысла"
#     return a**b
# a = int(input('A = '))
# b = int(input('B = '))
# print(f"{a} в степени {b} = {zad(a, b)}")



def zad(a, b):
    if a < 0 or b < 0:
        return "Не соответствует условию"
    if a == 0:
        return b
    else:
        return zad(a - 1, b + 1)
a = int(input('A = '))
b = int(input("B = "))
print(f"Сумма {a} и {b} равна {zad(a, b)}")