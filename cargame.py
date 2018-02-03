import pygame
import time
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)
red= (255,0,0)
green=(0,255,0)
display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sangram race')

clock = pygame.time.Clock()
carimg = pygame.image.load('car.jpg')

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def score(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged:"+str(count),True,black)
    gameDisplay.blit(text,(0,0))
    
def car(x,y):
    gameDisplay.blit(carimg,(x,y))

def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()
    
def message_display(text,color):
    largetext=pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect = text_objects(text,largetext,color)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    
    time.sleep(2)
    game_loop()

def crash(text,color):
    message_display(text,color)

def game_loop():
    gameExit = False
    x = (display_width*0.45)
    y = (display_height *0.8)
    x_change = 0
    car_speed = 0
    car_width=200
    thing_startx=random.randrange(0,display_width-100)
    thing_starty=-300
    thing_speed =7
    thing_width =100
    thing_height =100
    
    dodge=0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0

        x+=x_change            
        
        gameDisplay.fill(white)

    #things(thingx,thingy,thingw,thingh,color

        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty+=thing_speed
        car(x,y)
        score(dodge)

        if x==0 or x>display_width-50:
            crash('You Crashed',red)

        if thing_starty > display_height:
            thing_starty =0-thing_height
            thing_startx=random.randrange(0,display_width-100)
            dodge+=1
            if thing_speed <15:
                thing_speed+=1
            else:
                thing_speed=7
            
            

        if y<thing_starty+thing_height:
            if x>thing_startx and x<thing_startx+thing_width:
                crash('You Crashed',red)
            if x+45>thing_startx and x+45<thing_startx+thing_width:
                crash('You Crashed',red)
        pygame.display.update()
        clock.tick(100)

game_loop()
pygame.quit()
quit()
