import random
import time
def intro():
	print('you are in a forest and you are infront of two cave each cave has dragon as its guardian ,One dragon is kind and gives you the way to treasure,But the other is very hungry for a human flesh...Your task is to find  the treasure without giving your flesh as dragons meal..') 
def choosecave():
	cave = ' '
	while cave != '1' and cave != '2':
		print ('which cave you choose (1,2)')
		cave = input()
		return cave
def checkCave(chosencave):
	print ('You have approched the cave')
	time.sleep(2)
	print('Its dark and spooky')
	time.sleep(2)
	print('A dragon jumps infront of you !opening its large jaws and.....')
	time.sleep(2)
	friendlyCave=random.randint(1,2)
	print friendlyCave
	if chosencave == friendlyCave:
		print ('Gives you the treasure')
	else: 
		print ('Gobbles you down in one bite')
	
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	intro()
	caveNumber = choosecave()
	checkCave(caveNumber)
	print ('Do you want to playn the game again?(yes/no)')
	playAgain = input()
