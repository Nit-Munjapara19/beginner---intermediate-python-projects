import random
n=random.randint(1,100)
guesses_count=0
print("Gusses a number between 1 to 100")

while True:
    
    a=int(input("Enter your guess : "))
    guesses_count=guesses_count +1
  
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")    
    elif(a==n):
        print("you won this game")
        break

print(f"Your total guesses is {guesses_count}")        


