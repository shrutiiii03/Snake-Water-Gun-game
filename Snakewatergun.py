import random

while(True):
    a=input("0 to exit type ur choice snake gun water  ").lower()
    if a=='0':
      print("thank you for playing")
      break
    b=random.choice(['snake','water','gun'])
    print("user choice:  ",a)
    print("computer choice:  ",b)
    
    if a == b:
        print("It's a draw!")
    elif (a == 'snake' and b == 'water') or (a == 'water' and b == 'gun') or (a == 'gun' and b == 'snake'):
        print("User wins! Computer loses.")
    else:
        print("User loses! Computer wins.")
    