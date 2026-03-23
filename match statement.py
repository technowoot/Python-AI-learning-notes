#match statement
"""
格式
match 表达式：
    case 值1：
        操作1
    case 值2：
        操作2
    case 值3：
        操作3
    case 值4|值5：            # 二者成立一个即可执行
        操作4
    case _:                  # 其他都未被执行，执行他
        操作5
"""
# match语句自带“break”，一旦匹配成功，执行完匹配成功的语句后自动退出