'''
1 for stone
-1 for paper
0 for scissors
'''
import random

print("Let's Play stone paper scissors game :")
print('''
        a  for  stone   
        b  for  paper   
        c  for  scissors
      ''')

a="stone"
b="paper"
c="scissors"

computer=random.choice([1,0,-1])
you_chose = input("Enter Youer Choise : ")

Dictionary={'a':1,'b':-1,'c':0}
reverseddic={1:"stone",-1:"paper",0:"scissors"}

you=Dictionary[you_chose]

print(f"You chose {reverseddic[you]} and Computer chose {reverseddic[computer]} ")

if(computer==you):
    print("It's a draw")
else:    
     if (computer==1 and you==0):
       print("Lose!")
     elif(computer==1 and you==-1):
         print("Win!")    
     elif(computer==0 and you==1):
       print("Win!")    
     elif(computer==0 and you==-1):
       print("Lose!")        
     elif(computer==-1 and you==1):
       print("Lose!")    
     elif(computer==-1 and you==0):
       print("Win!")            