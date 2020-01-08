import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if ((50<pos[0] and pos[0]<150) and (50<pos[1] and pos[1]<100)):
                pygame.draw.rect(screen, (128, 128, 128), (50,50,100,50))
            if ((150<pos[0] and pos[0]<250) and (100<pos[1] and pos[1]<200)): 
                pygame.draw.rect(screen, (128, 128, 128), (150,100,100,100))
            if ((150<pos[0] and pos[0]<250) and (200<pos[1] and pos[1]<250)):
                pygame.draw.rect(screen, (128, 128, 128), (150,200,100,50))
            # if ((50<pos[0] and pos[0]<150) and (50<pos[1] and pos[1]<100)):
            #pygame.draw.rect(screen, (128, 128, 128), (50,50,100,50))
            # if ((150<pos[0] and pos[0]<250) and (100<pos[1] and pos[1]<200)):
            #pygame.draw.rect(screen, (128, 128, 128), (50,50,100,50))
            # if ((200<pos[0] and pos[0]<250) and (200<pos[1] and pos[1]<250)):
            #pygame.draw.rect(screen, (128, 128, 128), (50,50,100,50))
            # if ((50<pos[0] and pos[0]<150) and (50<pos[1] and pos[1]<100)):
            #pygame.draw.rect(screen, (128, 128, 128), (50,50,100,50))
            # if ((150<pos[0] and pos[0]<250) and (100<pos[1] and pos[1]<200)):
            #pygame.draw.rect(screen, (128, 128, 128), (50,50,100,50))
            # if ((200<pos[0] and pos[0]<250) and (200<pos[1] and pos[1]<250)):
            #pygame.draw.rect(screen, (128, 128, 128), (50,50,100,50))
        # Check to see if the current event is a QUIT event
    # main code goes here
    pygame.draw.line(screen, (255, 255, 255), (50, 100), (350, 100), 1)
    pygame.draw.line(screen, (255, 255, 255), (50, 200), (350, 200), 1)
    pygame.draw.line(screen, (255, 255, 255), (150, 50), (150, 250), 1)
    pygame.draw.line(screen, (255, 255, 255), (250, 50), (250, 250), 1)
    pygame.display.flip()
