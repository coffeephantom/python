# -*- coding: utf-8 -*-
import random


# 题目中对于激活码的格式并没有要求，目前采取这种策略
def generate_copoun():
    copoun = []
    copoun.append(str(random.randint(0, 200)))
    return copoun
