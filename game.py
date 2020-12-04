import math

def get_exp_for_lvl(level: int, factor:int):
    return factor*level*(level+1)

def get_lvl_for_exp(exp:int,factor:int):
    return math.floor((math.sqrt((factor/2)**2+100*exp)-factor/2)/50)

print(get_exp_for_lvl(3, 50))
print(get_lvl_for_exp(300,50))