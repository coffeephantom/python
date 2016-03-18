# -*- coding: utf-8 -*-


# 题目中对于激活码的格式并没有要求，目前采取这种策略
def generate_copoun():
    copoun = []
    for number in range(0, 200):
        copoun.append(str(number))
    return copoun
