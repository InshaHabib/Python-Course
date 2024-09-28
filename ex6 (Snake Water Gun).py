# Snake Water Gun
"""Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" 
where players use hand gestures to represent a snake,
water, or a gun. The gun beats the snake, the water beats the gun, and
the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements.
Do not create any fancy GUI. Use proper functions to check for win."""
#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

# Answer:
import random
def check(comp,user):
    if(comp==user):
        return 0
    elif(comp==0 and user==1):
        return -1
    elif(comp==1 and user==2):
        return -1
    elif(comp==2 and user==0):
        return -1
    return 1

    
comp=random.randint(0,2)
user=int(input("0 for snake, 1 for water and 2 for gun=\n"))
score=check(comp, user)
print(f"You={user}")
print(f"Computer={comp}")
if score==0:
    print("Its a Draw")
elif score==-1:
    print("You Lose")
else:
    print("You Won")