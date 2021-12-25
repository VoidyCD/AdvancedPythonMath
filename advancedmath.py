import math
pi = 3.14159



def cric(raidus: int):
    cirfum = 2 * pi * raidus
    return(cirfum)

def pytha(leg_a: int, leg_b: int):
    x =  math.pow(leg_a, 2) + math.pow(leg_b, 2)
    leg_c = math.sqrt(x)
    return(leg_c)

def avg(array: list):
    y = array.len()
