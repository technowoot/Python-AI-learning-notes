# 创建一个函数
"""
要求：输入一个或多个字母和数字的组合，    输入超限提示重新输入(长度大于1 )
                                    若其不是实数或小于0的实数，返回NULL
                                    是自然数，返回阶乘
                                    是大于0的小数，返回据其最近的那个整数的阶乘
                                    小数部分为0.5，则向上取整
"""
def factorial_step2(number):
    """
    这是阶乘计算的第二步，计算第一步传入的整数的阶乘
    :param number:整数
    :return:整数的阶乘
    """
    if number == 0:
        return 1
    else:
        return number * factorial_step2(number-1)

def factorial_step1(number):
    """
     这是阶乘计算的第一步，先将传入的数按照规则转化为对应整数，再传给第二步计算
    :param number: 传入的数
    :return: 对应整数
    """
    number = judge(number)
    return factorial_step2(number)

def judge(number):
    """
    这个函数会将传入的数按照规则转化为相应整数
    :param number: 传入的数
    :return: 对应整数
    """
    if number%1 ==0:
        return number
    else:
        if number%1==0.5:
            return number+0.5
        else:
            return round(number)
print("这段代码会为你计算一个数字的阶乘")
while 1:
    num = input("请输入一个数字，长度小于等于三位：")
    if len(num) >3:
        print("你输入的长度不对，请重新输入：")
        continue
    if not num.replace(".","",1).isdigit():
        print("输入的不是数字哦，请重新输入：")
        continue
    break
result = factorial_step1(float(num))
print(f"你输入数字的阶乘为：{result}")