import pygame
import random

def cubeGenerator():
	listCube = [[[1,1],[1,1]],[[1,1,1],[0,1,0]]]
	color = (random.randint(10,255),random.randint(10,255),random.randint(10,255))
	#color = (255,255,255)
	forme = (20,20,30,30)
	cube = [color,forme]
	return(cube)

def descente(cube,step):
	x1 = cube[1][0]
	x2 = cube[1][1]
	y1 = cube[1][2]
	y2 = cube[1][3]
	forme = (x1,x2+step,y1,y2)
	return(forme)

def moveLateral(cube,event,step):
	x = cube[1][0]
	if event.key == pygame.K_LEFT:
		x = x-step
	elif event.key == pygame.K_RIGHT:
		x = x+step
	forme = (x,cube[1][1],cube[1][2],cube[1][3]) 
	return(forme)

def formeDuBas(cube,formeDuBas=0):
	if formeDuBas == 0:
		return(cube)
	else :
		return(cube)

def drawFormeDuBas(formeDuBas,screen):
	for i in formeDuBas:
		pygame.draw.rect(screen, i)

if __name__ == '__main__':

	pygame.init()
	gameDisplay = pygame.display.set_mode((300,400))
	pygame.display.set_caption('Tetris')

	running = True
	while running:
		pygame.display.update()
		obj = cubeGenerator()
		base = (0,350,300,0)
		step = 30

		while running :			
			forme = descente(obj, step)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
						forme = moveLateral(obj,event,step)

			obj[1] = forme
			gameDisplay.fill(0)
			pygame.draw.rect(gameDisplay,obj[0],obj[1])
			pygame.draw.rect(gameDisplay,(255,255,255),base[1])
			#drawFormeDuBas()
			pygame.display.flip()
			pygame.event.clear()
			objt.bas = obj[1][1]-obj[1][2]
			base.hau = base[2]
			if objt.bas <= base.haut :
				obj = cubeGenerator()
			pygame.time.wait(1000)
		
		#if px == 301:
		running = False



# kaina 
# nacime
# mateo
# laura