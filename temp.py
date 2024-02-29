# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cmath

def solve_quadratic(a, b, c):
    # 計算判別式
    discriminant = (b ** 2) - (4 * a * c)

    # 判斷方程式是否有實根
    if discriminant >= 0:
        # 實根
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    else:
        # 虛根
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# 使用者輸入a, b, c的值
a = float(input("請輸入a的值："))
b = float(input("請輸入b的值："))
c = float(input("請輸入c的值："))

# 解一元二次方程式
root1, root2 = solve_quadratic(a, b, c)

# 輸出結果
print("方程式的解為:")
print("x1 =", root1)
print("x2 =", root2)
