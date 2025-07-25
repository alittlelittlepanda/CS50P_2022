# 输入苹果的价格
apple_price = input("请输入苹果的价格：")
apple_price = float(apple_price)

# 输入苹果的重量
apple_weight = input("请输入苹果的重量：")
apple_weight = float(apple_weight)

# 计算最终的价格
money = apple_price * apple_weight
print("请支付", money, "元", sep='', end='\n')