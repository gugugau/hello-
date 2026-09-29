print("=== 智能计算器 (输入 q 退出) ===")

while True:
    user_input = input("请输入算式 (例如 1+2): ")
    
    if user_input == 'q':
        print("计算器已退出。")
        break
        
    try:
        result = eval(user_input)  # eval 会计算字符串里的数学表达式
        print(f"结果: {result}")
    except:
        print("输入格式有误，请重新输入！")
