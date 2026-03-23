# 1.计算5到100(包含左端点，不包含右端点)之间数字之和
total_1 =0
for i in range(5,100):
    total_1 += i
print(total_1)

# 2.计算5到100(包含左端点，不包含右端点)间，所有为3的倍数的数字之和
total_2 =0
for i in range(6,100,3):
    total_2 += i
print(total_2)