import random
result = [['D','W','L'],['L','D','W'],['W','L','D']]
choice = ['Snake','Water','Gun']
userWin = 0
ComputerWin = 0
DrawMatch = 0
round = 0

while (True) :
  print(f"\n--------- Round {round+1} -------------")
  print("Choose any of the number below : \nSnake--0 \nWater--1 \nGun--2 \nExit--3")
  userChoice = int(input())
  computerChoice = random.randrange(0,2)

  if (userChoice==3) :
    break
  elif(userChoice>3 or userChoice<0):
    print("Please enter vaild input!!")
    continue
  round+=1
  print(f"\nRount {round} Result :-")
  print("User Choice:- "+choice[userChoice])
  print("Computer Choice:- "+choice[computerChoice])
  if (result[userChoice][computerChoice])== 'D':
    print("Match is Draw")
    DrawMatch+=1

  elif (result[userChoice][computerChoice])== "W":
    print("User is Win")
    userWin+=1

  else :
    print("Computer is Win")
    ComputerWin+=1
  
print("---------------------------------")
print("Overall Result:-")
print(f"Total Match : {round}")
print(f"Win of User : {userWin}")
print(f"Win of Computer : {ComputerWin}")
print(f"Draw Match : {DrawMatch}")
