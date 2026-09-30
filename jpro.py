print("=== 进阶计算器 (输入 q 退出) ===")

while True:
    a = input("请输入第一个数字 (或 q 退出): ")
    if a == 'q':
        break
        
    op = input("请输入运算符 (+ - * /): ")
    b = input("请输入第二个数字: ")

    try:
        num1 = float(a)
        num2 = float(b)
        
        if op == '+':
            print(f"结果: {num1 + num2}")
        elif op == '-':
            print(f"结果: {num1 - num2}")
        elif op == '*':
            print(f"结果: {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("错误：除数不能为0！")
            else:
                print(f"结果: {num1 / num2}")
        else:
            print("未知运算符！")
            
    except ValueError:
        print("输入的不是有效数字，请重新输入！")

print("计算器已退出。")
