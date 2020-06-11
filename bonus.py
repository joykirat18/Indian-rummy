import random
import pygame
import os
from textbox import *
from pygame.locals import *
import time

def playercards():
	"""this functions choose randomly 13 cards from the deck of cards"""
	player_cards = []
	for i in range(13):
		random_card = random.choice(allcards)
		allcards.remove(random_card)
		player_cards.append(random_card)
	return player_cards

def convertjoker(deck):
	"""all the cards cooresponding to rank same as that of the first card
	of the stockpile is converted to joker"""
	for i in range(len(deck)):
		if deck[i][:-1]==joker:
			deck[i]="Joker"
	return deck

def swap(deck):
	"""Helps user arrange the cards in the game"""
	print("Swap Card")
	change = input1("swap(firstcard _ secondcard)",screen)
	change = change.split()
	change1=[]
	for i in change:
		i = int(i)
		change1.append(i)
	card1=change1[0]
	card2=change1[1]
	deck[card1-1],deck[card2-1]=deck[card2-1],deck[card1-1]
	print(player1_cards)

def movetodiscard(stockpile):
	"""moves the card from the stockpile to the discardpile"""
	discardpile.append(stockpile[0])
	stockpile.remove(stockpile[0])

# def choosecard():
	# flag = input()
	# if flag == "yes":
		# player1_cards.append(discardpile[-1])
	# else:
		# player1_cards.append(stockpile[0])
		# stockpile.remove(stockpile[0])

def path(card):
	"""helps find the path of the image of the cards in the computer"""
	return os.path.join(os.getcwd(),"PNG",card+'.png')

def sort_cards(deck):
	#sorts the cards based on their rank
	print("Sort Card")
	global value
	# push joker to end
	count = 0
	for i in deck:
		if i == 'Joker':
			count += 1
	for i in range(count):
		deck.remove("Joker")		

	# custom sort of deck (bubble sort)
	n = len(deck)
	for i in range(n - 1):
		for j in range(n - 1 - i):
			if value[deck[j][:-1]] > value[deck[j + 1][:-1]]:
				deck[j], deck[j + 1] = deck[j + 1], deck[j]
	# player()

	for i in range(count):
		deck.append("Joker")

def drop_card(deck): 
	"""choose the card from the deck you want to drop from the deck
	the choosen card moves to the dicardpile"""
	global turn
	print("Drop card")
	global discardpile
	if(len(deck)<14):
		textbox(screen,"Length should be 14. Enter to continue.")
		# fontobject = pygame.font.Font(None,29)			
		while key1()!= K_RETURN:
			pass
		return		
	drop = input1("Drop card number",screen)
	card = deck[int(drop)-1]
	deck.remove(card)
	discardpile.append(card)
	turn = 1
	

def pickStockPile(deck):
	"""picks the card from the stockpile"""
	if(len(deck)==13):
		card = stockpile[0]
		deck.append(card)
		stockpile.remove(card)
		textbox(screen,"Enter to continue.")
		while key1()!= K_RETURN:
			pass
	else:
		textbox(screen,"Number of cards is 14.Connot pick.Enter to continue.")
		while key1()!= K_RETURN:
			pass

def pickDiscardPile(deck):
	"""picks the card from the dicardpile"""
	if(len(deck)==13):
		card = discardpile[len(discardpile)-1]
		deck.append(card)
		discardpile.remove(card)
		textbox(screen,"Enter to continue.")
		while key1()!= K_RETURN:
			pass
	else:
		textbox(screen,"Number of cards is 14.Connot pick.Enter to continue.")
		while key1()!= K_RETURN:
			pass

def is_pure(seq):
	"""checks whether the sequence is pure or not"""
	suits = []
	num = ""
	for i in seq:
		if i == 'Joker':
			return False#seq cannot be pure if it has joker
		suits.append(i[-1])
		num += i[:-1]

	for i in range(len(suits) - 1):
		if suits[i]!=suits[i+1]:#all the suits of the cards should be similar
			return False	

	if num not in RUNS:#cards should be arranged in an order
		return False

	return True

def is_set(seq):
	suits = []
	num = []

	if('Joker' in seq):
		seq.remove('Joker')
		# set cannot have more than 1 Joker
		if('Joker' in seq):
			return False	
	for i in seq:
		suits.append(i[-1])
		num.append(i[:-1])

	for i in range(len(num)-1):
		if(num[i]!=num[i+1]):#all the ranks of the seq should be equal
			return False
	print("suit: ", suits)
	suits.sort()
	for i in range(len(suits)-1):
		if(suits[i]==suits[i+1]):#all the suits of the seq should be different
			return False

	return True

def is_impure(seq):
	suits = []
	num = ""
	count=0
	for i in seq:
		if(i=='Joker'):
			count+=1
	if(count>1):
		print("Failing on more than 1 joker")
		return False#number of jokers cannot be more than 1

	for i in range(len(seq)):
		print("Impure:",seq[i])
		if(seq[i] == 'Joker'):
			if(i==0):#helps to identify what value should joker have so that the ranks are in a order
				num+=value2[str(value[seq[i+1][:-1]]-1)]
			else:
				num+=value2[str((value[seq[i-1][:-1]])%13+1)]	
		else:	
			suits.append(seq[i][-1])
			num+=seq[i][:-1]

	print("Suits : ", suits)
	print("Num: ", num)		

	for i in range(len(suits) - 1):
		if suits[i]!=suits[i+1]:
			print("Suits are not matching")
			return False#all the suits should be same

	if num not in RUNS:
		print("Not a subsequence")
		return False#ranks should be in order

	return True

def declare2(sets):
	"""helper function for computer's cards"""
	count_valid=0
	count_valid_joker=0
	count_impure = 0
	for i in sets:
		print(i)
		if(is_pure(i)):
			print(i, "is pure")
			count_valid+=1
		elif(is_impure(i)):
			count_valid_joker += 1
		print("-----------------")

	for i in sets:
		if len(i)==4:#a run of 4 cards should be either impure or pure
			if is_pure(i)==False and is_impure(i)==False:
				return False

	print(count_valid, count_valid_joker)
	if count_valid == 0:
		return False

	if count_valid + count_valid_joker < 2:
		return False#there should be atleast 2 runs(including 4 cards)

	for i in sets:
		if not is_pure(i) and not is_impure(i) and not is_set(i):
			return False

	return True


def com_declare(deck):
	print(deck)
	set1=[deck[:3],deck[3:6],deck[6:9],deck[9:]]#assuming 3,3,3,4 order
	set2=[deck[:3],deck[3:6],deck[6:10],deck[10:]]#assuming 3,3,4,3 order
	set3=[deck[:3],deck[3:7],deck[7:10],deck[10:]] #assuming 3,4,3,3 order
	set4=[deck[:4],deck[4:7],deck[7:10],deck[10:]]#assuming 4,3,3,3 order
	
	if declare2(set1) == True or declare2(set2) ==True or declare2(set3) ==True or declare2(set4)==True:
		return True
	else:
		return False

def declare(deck):
	# assume 4,3,3,3 sequence
	sets=[deck[:4],deck[4:7],deck[7:10],deck[10:]]
	count_valid=0
	count_valid_joker=0
	for i in sets:
		print(i)
		if(is_pure(i)):
			print(i, "is pure")
			count_valid+=1
		elif(is_impure(i)):
			count_valid_joker += 1
		print("-----------------")

	for i in sets:
		if len(i)==4:
			if is_pure(i)==False and is_impure(i)==False:
				return False
	print(count_valid, count_valid_joker)
	if count_valid == 0:
		return False

	if count_valid + count_valid_joker < 2:
		return False

	for i in sets:
		if not is_pure(i) and not is_impure(i) and not is_set(i):
			return False

	return True

def declarePlayer(deck):
	"""checks the condition whether the in sequence or not"""
	if(declare(deck)):
		print("Win")
		winmusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","win"+'.mp3')))
		pygame.mixer.music.play()
		textbox(screen,"You win. Enter to exit")
		while key1()!= K_RETURN:
			pass
		exit()
	else:
		print("Lose")
		losemuisc = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","lose"+'.mp3')))
		pygame.mixer.music.play()
		textbox(screen,"You lose. Enter to exit.")
		while key1()!= K_RETURN:
			pass
		exit()


def draw_button(x,y,w,h,text):
	#create button
	global screen
	pygame.draw.rect(screen,(0,0,0),(x,y,w,h))#create rectangle
	font = pygame.font.Font("freesansbold.ttf", 16)
	text1 = font.render(text,True,(255,255,255))#adding a text
	text2 = text1.get_rect()
	text2.center = ((x+(w/2)), (y+(h/2)))
	screen.blit(text1,text2)
	return x,y,w,h

def onClick(x,y,w,h,func,deck):
	mouse_position = pygame.mouse.get_pos()
	click_event = pygame.mouse.get_pressed()#gets the positon of mouse
	if click_event[0]==1:#if the mouse is clicked
		if x<mouse_position[0]<x+w and y<mouse_position[1]<y+h:#mouse is inside the button
			clickmusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","click"+'.mp3')))

			pygame.mixer.music.play()
			if func==drop_card:
				func(deck)
				com()
				# time.sleep(1)
			else:
				func(deck)	




def player():
	# global turn
	global player1_cards
	global computer_back
	# print(player1_cards)
	# pausetimerevent = pygame.USEREVENT + 1
	cards_image = []
	com_image=[]
	# print("length of player cards : ", len(player1_cards))
	for i in player1_cards:
		cards_image.append(pygame.image.load(path(str(i))))#storing the image in a list
	for i in computer_back:
		com_image.append(pygame.image.load(path(str(i))))


	#loading the images into pygame
	stockcard = pygame.image.load(path(str(stockpile[0])))
	discardcard = pygame.image.load(path(str(discardpile[-1])))
	emptycard = pygame.image.load(path("gray_back"))
	intromusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","intro"+'.mp3')))
	losemuisc = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","lose"+'.mp3')))
	clickmusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","click"+'.mp3')))
	shufflemusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","shuffle"+'.mp3')))
	winmusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","win"+'.mp3')))
	#displaying the image on the screen
	for i in range(len(player1_cards)):
		screen.blit(cards_image[i], (cards_x[i], cardy))

	for i in range(len(computer_back)):
		screen.blit(com_image[i],(cards_x[i],comy))
	screen.blit(stockcard,(stockcardx,stockcardy))
	screen.blit(discardcard,(discardcardx,discardcardy))
	screen.blit(emptycard,(stockcardx,stockcardy))



	#defining 6 differnt buttons 
	sort_button = draw_button(50,500,80,40,"SORT")
	swap_button = draw_button(50,400,80,40,"SWAP")
	drop_button = draw_button(50,450,80,40,"DROP")
	stock_button = draw_button(650,400,120,40,"PICK FROM SP")
	discard_button = draw_button(650,450,120,40,"PICK FROM DP")
	declare_button = draw_button(650,500,120,40,"DECLARE")

	#"*" infront of the buttons helps to unpack the sequence
	onClick(*sort_button,sort_cards,player1_cards)
	
	onClick(*swap_button,swap,player1_cards)
	# wait()
	onClick(*drop_button,drop_card, player1_cards)
	# wait()
	onClick(*stock_button,pickStockPile,player1_cards)
	# wait()
	onClick(*discard_button,pickDiscardPile,player1_cards)
	# wait()
	onClick(*declare_button,declarePlayer,player1_cards)

		# pygame.time.set_timer(pausetimerevent, 2000)

def menu():
	intromusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","intro"+'.mp3')))
	pygame.mixer.music.play()
	rummy = pygame.image.load(path(str(os.path.join(os.getcwd(),"PNG","rummy"))))
	cardphoto = pygame.image.load(path(os.path.join(os.getcwd(),"PNG","cardphoto")))
	screen1.blit(cardphoto,(0,0))
	screen1.blit(rummy,(150,0))

	fontobject = pygame.font.Font(None,29)	
	screen1.blit(fontobject.render("", 10,(0,255,0),(100,560)),(260,565))
	pygame.draw.rect(screen1,(22,108,16),(200,560,390,30))
	name = input1("Please press enter to play",screen1)
	pygame.display.update()


def com():
	"""this is the computer algorithm which is totally random """
	global discardpile
	global stockpile
	
	# sort_cards(computer_cards)
	pile = random.choice([0,1])
	print(computer_cards)
	print(pile)
	
	if pile ==0:
		#choose from dicard pile
		card = discardpile[len(discardpile)-1]
		computer_cards.append(card)
		discardpile.remove(card)
		#choose any random card and drops it
		card = computer_cards[int(random.randint(1,13))-1]
		computer_cards.remove(card)
		discardpile.append(card)

	if pile ==1:
		#choose from stockpile	
		card = stockpile[0]
		computer_cards.append(card)
		stockpile.remove(card)
		#choose any random card and drops it
		card = computer_cards[int(random.randint(1,13))-1]
		computer_cards.remove(card)
		discardpile.append(card)
	if com_declare(computer_cards)==True:
		#if computer was successful in making a set
		textbox(screen,"The computer won the game")


allcards = ["AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH"]

# player1 = input("enter the name of player 1 ")

symbols = ["⬥","♥","♣","♠"]
character = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
value = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
value2 = {"1":"A","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","11":"J","12":"Q","13":"K"}
suits = ["hearts","diamond","clubs","spades"]
suit_value={"⬥":"diamonds","♥":"hearts","♣":"clubs","♠":"spades"}
discardpile=["gray_back"]
RUNS = "A2345678910JQKA"
# print(len(allcards))
player1_cards = playercards()
# player1_cards = ['AS','AC','Joker','2C','3C','4C','QH','KH','Joker','9C','10C','Joker','QC']
computer_cards = playercards()
computer_back = ["blue_back","blue_back","blue_back","blue_back","blue_back","blue_back","blue_back","blue_back","blue_back","blue_back","blue_back","blue_back","blue_back"]

# print(allcards)
random.shuffle(allcards)
joker = allcards[0][:-1]
# print(joker)
allcards.remove(allcards[0])
stockpile = allcards
movetodiscard(stockpile)
# choosecard()
convertjoker(player1_cards)
convertjoker(computer_cards)
convertjoker(allcards)
print(discardpile)
print(stockpile)
print(player1_cards)
# sort_cards(computer_cards)
print(computer_cards)


pygame.init()
screen = pygame.display.set_mode((800,600))
screen1 = pygame.display.set_mode((800,600))

running = True

cards_x = [i for i in range(170, 170 + 30*14, 30)]
# card1x=170
# card2x = 200
comy =60
cardy = 400 
stockcardx = 300
stockcardy = 200
discardcardx = 200
discardcardy = 200 
print("print 129")

screen1.fill((255,255,255))
menu()
pygame.mixer.music.stop()
pygame.display.update()


	

while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running = False
	screen.fill((22,108,16))
	# time.sleep(1)
	shufflemusic = pygame.mixer.music.load(str(os.path.join(os.getcwd(),"sound","shuffle"+'.mp3')))
	pygame.mixer.music.play()
	player()
	

	pygame.display.update()
	pygame.display.flip()
	pygame.display.update()














