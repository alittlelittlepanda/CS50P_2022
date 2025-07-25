father_height = input("请输入父亲的身高：")
father_height = float(father_height)

mother_height = input("请输入母亲的身高：")
mother_height = float(mother_height)

son_height = (mother_height + father_height) * 0.54
print("儿子的身高是：", son_height, "m")
