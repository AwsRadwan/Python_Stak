import random
def randInt(max=100 , min=0):
    num = round(random.random()*(max-min) + min)
    return num
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
