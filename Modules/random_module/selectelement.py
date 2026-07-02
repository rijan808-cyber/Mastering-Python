from random import *
l = ["Mango","Apple","Cherry","Grapes","Orange","Banana","Pineapple"]
print(choice(l))
print(choices(l, k=3))
print(sample(l, k=5))
shuffle(l)
print(l)