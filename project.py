money = int(input())
price_a =int(input())
price_b =int(input())
number =0
while money>=(price_a+price_b):
    number += 1
    money -= (price_b+price_a)
print(number)