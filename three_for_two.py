def mango(quantity, price):
    import math
    return (quantity - math.floor(quantity/3)) * price

mango(3,3)
#should return 6