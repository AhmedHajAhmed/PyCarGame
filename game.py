# import libraries 
import pygame 
from pygame.locals import * 
import random
import time 



# set size (in px)
size = width, height = (800, 800)

# set road settings 500 px (800/1.6)
road_w = int(width/1.6) 

# set road marking 10 px
roadmark_w = int(width/80)

# set right lane 
right_lane = width/2 + road_w/4

# set left lane 
left_lane = width/2 - road_w/4 

# initilize speed, starting with 1 
speed = 1


# initialize game 
pygame.init()

# create var
running = True

# define screen (display)
screen = pygame.display.set_mode(size)

# set caption (game/tap title)
pygame.display.set_caption("PyCarGame")

# set background color 
screen.fill((162, 26, 52))


# update display settings 
pygame.display.update()


# load your car
me = pygame.image.load("./utils/car.png")
me_loc = me.get_rect()
me_loc.center = right_lane, height*0.8

# load enemy car 
Dave = pygame.image.load("./utils/otherCar.png")
Dave_loc = Dave.get_rect()
Dave_loc.center = left_lane, height*0.2

# load crash audio 
laugh_sound = pygame.mixer.Sound("./utils/crash_sound.wav")



# create counter to keep track of number of times the player succeeds to run away from enemy 
counter = 0 

# create an event listener that waits for the user to click on the exit button, and then after quit gmae 
while running:

    counter += 1
    if counter == 5000:
        speed += 0.10
        counter = 0
        print("Level up:", speed)

    # animate enemy vehicle by changing the height (index 1)
    Dave_loc[1] += speed
    if Dave_loc[1] > height:
        # randomize lanes (left & right)
        if random.randint(0, 1) == 0:
            Dave_loc.center = right_lane, -200
        else:
            Dave_loc.center = left_lane, -200 

    # end game (in case of collision)
    if me_loc[0] == Dave_loc[0] and Dave_loc[1] > me_loc[1] -245:
        laugh_sound.play()
        time.sleep(1.8)
        break

    # itereate over all the events in the game 
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False 

        # if user press on a button 
        if event.type == KEYDOWN: 

            # if user press left button 
            if event.key in [K_a, K_LEFT]:
                me_loc = me_loc.move([-int(road_w/2), 0])

            # if user press right button 
            if event.key in [K_d, K_RIGHT]:
                me_loc = me_loc.move([int(road_w/2), 0])



    # draw road 
    pygame.draw.rect(screen, (50, 50, 50), (width/2 - road_w/2, 0, road_w, height))


    # draw road mark
    pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))


    # draw pics 
    screen.blit(me, me_loc)
    screen.blit(Dave, Dave_loc)


    pygame.display.update()



# close game
pygame.quit()

