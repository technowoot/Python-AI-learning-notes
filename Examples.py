# 一些基础的函数

# 1.根据传入的底和高计算三角形的面积(保留两位小数)
def area(height,length):
    """
    该函数根据传入的底和高计算三角形的面积，面积保留两位小数
    :param height:三角形的高
    :param length: 三角形的底
    :return: 三角形的面积
    """
    return round(height*length/2,2)

# 2。定义一个函数，计算传入字符串中元音字母的个数(大小写都算)
def count_aeiou(string):
    """
    该函数可以计算传入字符串中的元音字母的个数
    :param string: 传入的字符串
    :return: 元音字母的个数
    """
    number = 0
    for i in string:
        if i in "aeiouAEIOU":
            number += 1
    return number

# 3.定义一个函数，传入一个全是数字列表，输出这组列表在中的最大值，最小值，平均值
def calculator(number):
    """
    这个函数仅可传入全是数字的列表，输出这组数据的最大值，最小值，平均值
    :param number: 传入列表
    :return: 最大值，最小值，平均值
    """
    return max(number),min(number),round(sum(number),1)/len(number)

#  函数1的调用
print("输入一个三角形的底和高，输出这个三角形的面积")
length = float(input("请输入这个三角形的底:"))
height = float(input("请输入这个三角形的高:"))
area = area(height,length)
print("这个三角形的面积是%.1f"%area)

# 函数2的调用
string = input("输入一个字符串，输出这个字符串中元音字母的个数:")
number = count_aeiou(string)
print(f"这个字符串中元音字母的个数为{number}")

# 函数3的调用
asd1 = list(map(int,(input("输入一段数字，数字间以空格隔开输出这段数字中的最大值，最小值，平均值").split())))
max_num,min_num,ave=calculator(asd1)
print(f"这串数据的最大值为{max_num}，最小值为{min_num}，平均值为{ave}")
