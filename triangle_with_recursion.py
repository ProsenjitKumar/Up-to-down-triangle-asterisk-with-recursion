# Enter a Number: 4
# ****
# ***
# **
# *

def up_to_down_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print('' * ( t + 1 ) + '*' * i)
        return up_to_down_triangle( i - 1, t + 1 )

up_to_down_triangle(int(input("Enter a Number: ")))