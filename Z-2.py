#  Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
a = int(input("Введите положительное трехзначное число: "))
if a>=100 and a<1000:
    a1 = a//100
    a2 = a//10%10
    a3 = a%10
    b = a1+a2+a3
    print(b)
else:
    print("Число не положительное трехзначное")
