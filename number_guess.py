#Number guessing game in python


import random
n = random.randint(1,10)

print(" This game gives you 5 chances to guess! ")

guess = int(input("Enter a number between 1 to 10: "))
k=0
flag=0

while k < 5:
	if guess < n:
		print(k+1," Chances gone! Guess is low....Try again!")
		guess = int(input("Enter a number between 1 to 10: "))
		k = k+1
	elif guess > n:
		print(k+1," Chances gone! Guess is High....Try again!")
		guess = int(input("Enter a number between 1 to 10: "))
		k = k+1
	else:
		print("You Guessed right!")
		flag=1
		break

if flag == 0:
	print("Game over")





