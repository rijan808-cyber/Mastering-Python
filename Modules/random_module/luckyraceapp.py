from random import *
import time
player1 = "Cristiano Ronaldo"
player2 = "Lionel Messi"
player3 = "Kylien Mbappe"
player4 = "Earlin Haaland"
r=m=k=h=0
print()
print("Welcome to our Lucky race application")
print("__"*30)
while True:
    n=randint(1,6)
    print(f"{player1} = {n}")
    r=r+n
    time.sleep(2)

    n=randint(1,6)
    print(f"{player2} = {n}")
    m=m+n
    time.sleep(2)
    
    n=randint(1,6)
    print(f"{player3} = {n}")
    k=k+n
    time.sleep(2)
    
    n=randint(1,6)
    print(f"{player4} = {n}")
    h=h+n
    time.sleep(2)
    
    if r>10 and r>m and r>k and r>h:
        print(f"Congratulations!!!!! {player1} you have won suiiiiiii!!!!!!!!!!!")
        break
    elif m>10 and m>r and m>k and m>h:
        print(f"Congratulations!!!!! {player2} you have won!!!!!!!!!!!!!!!")
        break
    elif k>10 and k>m and k>m and k>h:
        print(f"Congratulations!!!!! {player3} you have won!!!!!!!!!!!!!!!")
        break
    elif h>10 and h>m and h>k and h>r:
        print(f"Congratulations!!!!! {player4} you have won!!!!!!!!!!!!!!")
        break
    else:
        pass

    print("__"*30)
    print()
print("__"*30)
print()