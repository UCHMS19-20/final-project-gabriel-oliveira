import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()
def give_color(clicked, hovering):
    if clicked:
        return (255, 255, 255)
    else:
        if hovering:
            return (128, 128, 128)
        else:
            return (0, 0, 0)
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )
clicked = [False, False, False, False, False, False, False, False, False]
hovered = [False, False, False, False, False, False, False, False, False]
# Main loop. Your game would go inside this loop
while True:


    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if ((50<pos[0] and pos[0]<150) and (50<pos[1] and pos[1]<100)):
                clicked[0]= True
            if ((150<pos[0] and pos[0]<250) and (100<pos[1] and pos[1]<200)):
                clicked[4]= True
            if ((150<pos[0] and pos[0]<250) and (200<pos[1] and pos[1]<250)):
                clicked[7]= True
            if ((50<pos[0] and pos[0]<150) and (100<pos[1] and pos[1]<200)):
                clicked[3]= True
            if ((150<pos[0] and pos[0]<250) and (50<pos[1] and pos[1]<100)):
                clicked[1]= True
            if ((50<pos[0] and pos[0]<150) and (200<pos[1] and pos[1]<250)):
                clicked[6]= True
            if ((250<pos[0] and pos[0]<350) and (50<pos[1] and pos[1]<100)):
                clicked[2]= True
            if ((250<pos[0] and pos[0]<350) and (100<pos[1] and pos[1]<200)):
                clicked[5]= True
            if ((250<pos[0] and pos[0]<350) and (200<pos[1] and pos[1]<250)):
                clicked[8]= True
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if ((50<pos[0] and pos[0]<150) and (50<pos[1] and pos[1]<100)):
                hovered[0]= True
                hovered[1]= False
                hovered[2]= False
                hovered[3]= False
                hovered[4]= False
                hovered[5]= False
                hovered[6]= False
                hovered[7]= False
                hovered[8]= False
            if ((150<pos[0] and pos[0]<250) and (100<pos[1] and pos[1]<200)):
                hovered[4]= True
                hovered[0]= False
                hovered[1]= False
                hovered[2]= False
                hovered[3]= False
                hovered[5]= False
                hovered[6]= False
                hovered[7]= False
                hovered[8]= False
            if ((150<pos[0] and pos[0]<250) and (200<pos[1] and pos[1]<250)):
                hovered[7]= True
                hovered[0]= False
                hovered[1]= False
                hovered[2]= False
                hovered[3]= False
                hovered[4]= False
                hovered[5]= False
                hovered[6]= False
                hovered[8]= False
            if ((50<pos[0] and pos[0]<150) and (100<pos[1] and pos[1]<200)):
                hovered[3]= True
                hovered[0]= False
                hovered[1]= False
                hovered[2]= False
                hovered[4]= False
                hovered[5]= False
                hovered[6]= False
                hovered[7]= False
                hovered[8]= False
            if ((150<pos[0] and pos[0]<250) and (50<pos[1] and pos[1]<100)):
                hovered[1]= True
                hovered[0]= False
                hovered[2]= False
                hovered[3]= False
                hovered[4]= False
                hovered[5]= False
                hovered[6]= False
                hovered[7]= False
                hovered[8]= False
            if ((50<pos[0] and pos[0]<150) and (200<pos[1] and pos[1]<250)):
                hovered[6]= True
                hovered[0]= False
                hovered[1]= False
                hovered[2]= False
                hovered[3]= False
                hovered[4]= False
                hovered[5]= False
                hovered[7]= False
                hovered[8]= False
            if ((250<pos[0] and pos[0]<350) and (50<pos[1] and pos[1]<100)):
                hovered[2]= True
                hovered[0]= False
                hovered[1]= False
                hovered[3]= False
                hovered[4]= False
                hovered[5]= False
                hovered[6]= False
                hovered[7]= False
                hovered[8]= False
            if ((250<pos[0] and pos[0]<350) and (100<pos[1] and pos[1]<200)):
                hovered[5]= True
                hovered[0]= False
                hovered[1]= False
                hovered[2]= False
                hovered[3]= False
                hovered[4]= False
                hovered[6]= False
                hovered[7]= False
                hovered[8]= False
            if ((250<pos[0] and pos[0]<350) and (200<pos[1] and pos[1]<250)):
                hovered[8]= True
                hovered[0]= False
                hovered[1]= False
                hovered[2]= False
                hovered[3]= False
                hovered[4]= False
                hovered[5]= False
                hovered[6]= False
                hovered[7]= False

        # Check to see if the current event is a QUIT event
    # main code goes here
   
    pygame.draw.rect(screen, give_color(clicked[8], hovered[8]), (250,200,100,50))
    pygame.draw.rect(screen, give_color(clicked[4], hovered[4]), (150,100,100,100))
    pygame.draw.rect(screen, give_color(clicked[7], hovered[7]), (150,200,100,50))
    pygame.draw.rect(screen, give_color(clicked[3], hovered[3]), (50,100,100,100))
    pygame.draw.rect(screen, give_color(clicked[1], hovered[1]), (150,50,100,50))
    pygame.draw.rect(screen, give_color(clicked[6], hovered[6]), (50,200,100,50))
    pygame.draw.rect(screen, give_color(clicked[2], hovered[2]), (250,50,100,50))
    pygame.draw.rect(screen, give_color(clicked[5], hovered[5]), (250, 100, 100, 100))
    pygame.draw.rect(screen, give_color(clicked[0], hovered[0]), (50,50,100,50))

    
    pygame.draw.line(screen, (255, 255, 255), (50, 100), (350, 100), 1)
    pygame.draw.line(screen, (255, 255, 255), (50, 200), (350, 200), 1)
    pygame.draw.line(screen, (255, 255, 255), (150, 50), (150, 250), 1)
    pygame.draw.line(screen, (255, 255, 255), (250, 50), (250, 250), 1)

    pygame.display.flip()
