"""
变量的命名和使用
在Python中使用变量时，需要遵守一些规则和指南。违反这些规则将引发错误，而指南旨在让你编写的代码更容易阅读和理解。请务必牢记下述有关变量的规则。
变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greetingmessage会引发错误。
不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print （请参见附录A.4）。
变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
要创建良好的变量名，需要经过一定的实践，在程序复杂而有趣时尤其如此。随着你编写的程序越来越多，并开始阅读别人编写的代码，将越来越善于创建有意义的变量名。
注意 就目前而言，应使用小写的Python变量名。在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的主意。
"""
# 1. 使用字符串方法转换大小写
print("执行代码段落1：")
str1 = "Hello, where are you"
# 使用title()方法使字符串首字母大写
str1_first_letter_upper = str1.title()
print(f"str1首字母大写后变成：{str1_first_letter_upper}")  # str1首字母大写后变成：Hello, Where Are You
# 使用upper()方法使字符串全部大写
str1_upper = str1.upper()
print(f"str1字母全部大写后是：{str1_upper}")  # str1字母全部大写后是：HELLO, WHERE ARE YOU
# 使用lower()方法使字母全部小写
str1_lower = str1.lower()
print(f"str1字母全部小写后是：{str1_lower}")  # str1字母全部小写后是：hello, where are you

# 使用 '+' 拼接字符串
print("\n\n执行代码段落2：")
first_name = 'michael'
last_name = 'jordan'
full_name = first_name + ' ' + last_name
print("Hello, " + full_name.title() + "!")  # Hello, Michael Jordan!
# 添加制表符\t和换行符\n
print("打印制表对齐的字符串：\n\tPython\n\tC++\n\tJavascript")
