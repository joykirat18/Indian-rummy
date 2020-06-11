import pygame
from pygame.locals import *

def key1():
	event = pygame.event.poll()
	if event.type == KEYDOWN:
		return event.key


def textbox(screen,message):
	fontobject = pygame.font.Font(None,29)	
	# pygame.draw.rect(screen,(0,150,0),(260,560,390,30))
	if len(message)!= 0:
		screen.blit(fontobject.render(message, 10,(255,255,255),(100,260)),(260,565))
	pygame.display.flip()

# def textbox_other(screen,message):
	# fontobject = pygame.font.Font(None,29)	
	# if len(message)!= 0:
		# screen.blit(fontobject.render(message, 10,(255,255,255),(100,260)),(260,350))
	# pygame.display.flip()	

def input1(text,screen):
	pygame.font.init()
	string = []
	textbox(screen,text + ":"+ "".join(string))

	while True:
		ans = key1()
		if ans == K_BACKSPACE:
			string = string[0:-1]
		elif ans == K_RETURN:
			break
		elif ans == K_SPACE:
			string.append(" ")		
		elif ans == K_0:
			string.append("0")
		elif ans == K_1:
			string.append("1")
		elif ans == K_2:
			string.append("2")
		elif ans == K_3:
			string.append("3")		
		elif ans == K_4:
			string.append("4")
		elif ans == K_5:
			string.append("5")		
		elif ans == K_6:
			string.append("6")		
		elif ans == K_7:
			string.append("7")
		elif ans == K_8:
			string.append("8")
		elif ans == K_9:	
			string.append("9")
		# elif ans == word():
		# 	string.append(ans[3:]) 
		# if ans == K_10:
		# 	string.append("10")
		# if ans == K_11:	
		# 	string.append("11")
		# if ans == K_12:
		# 	string.append("12")
		# if ans==K_13:
		# 	string.append("13")
		textbox(screen,text + "".join(string))
	return "".join(string)

def word():
	letter = input()
	return "K_" + "letter"


def main():
	screen = pygame.display.set_mode((800,600))
	print(input(screen))

if __name__ == '__main__': main()	





