import sys
import pygame

def check(a, b, c):
    if clicked[a] == 0:
        return False
    elif clicked[b] == 0:
        return False
    elif clicked[c] == 0:
        return False
    else:
        if clicked [a] % 2 == clicked[b] % 2:
            if clicked [a]%2 == clicked[c]%2:
                return True
            else:
                return False
        else:
            return False
# Initialize pygame so it runs in the background and manages things
pygame.init()
def give_color(clicked, hovering):
    #determine what color the box will turn when clicked or hovering
    if clicked != 0:
        if clicked % 2 == 0:
            return (255, 255, 255)
        else:
            return (255, 0, 0)
    else:
        if hovering:
            return (128, 128, 128)
        else:
            return (0, 0, 0)
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )
clicked = [0, 0, 0, 0, 0, 0, 0, 0, 0]
hovered = [False, False, False, False, False, False, False, False, False]
# Main loop. Your game would go inside this loop
total_clicks = 0
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            total_clicks += 1
            pos = pygame.mouse.get_pos() 
            #determine if number of clicks is even or odd
            if ((50<pos[0] and pos[0]<150) and (50<pos[1] and pos[1]<100)):
                if total_clicks % 2 == 0:
                    clicked[0] = 2
                else:
                    clicked[0] = 1
            if ((150<pos[0] and pos[0]<250) and (100<pos[1] and pos[1]<200)):
                if total_clicks % 2 == 0:
                    clicked[4] = 2
                else:
                    clicked[4] = 1
            if ((150<pos[0] and pos[0]<250) and (200<pos[1] and pos[1]<250)):
                if total_clicks % 2 == 0:
                    clicked[7] = 2
                else:
                    clicked[7] = 1
            if ((50<pos[0] and pos[0]<150) and (100<pos[1] and pos[1]<200)):
                if total_clicks % 2 == 0:
                    clicked[3] = 2
                else:
                    clicked[3] = 1           
            if ((150<pos[0] and pos[0]<250) and (50<pos[1] and pos[1]<100)):
                if total_clicks % 2 == 0:
                    clicked[1] = 2
                else:
                    clicked[1] = 1
            if ((50<pos[0] and pos[0]<150) and (200<pos[1] and pos[1]<250)):
                if total_clicks % 2 == 0:
                    clicked[6] = 2
                else:
                    clicked[6] = 1
            if ((250<pos[0] and pos[0]<350) and (50<pos[1] and pos[1]<100)):
                if total_clicks % 2 == 0:
                    clicked[2] = 2
                else:
                    clicked[2] = 1
            if ((250<pos[0] and pos[0]<350) and (100<pos[1] and pos[1]<200)):
                if total_clicks % 2 == 0:
                    clicked[5] = 2
                else:
                    clicked[5] = 1
            if ((250<pos[0] and pos[0]<350) and (200<pos[1] and pos[1]<250)):
                if total_clicks % 2 == 0:
                    clicked[8] = 2
                else:
                    clicked[8] = 1
        if event.type == pygame.MOUSEMOTION:
            #allow hover of boxes to be gray
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

    if check(0, 1, 2) == True:
        print("you win")
        break
    elif check(3,4,5) == True:
        print("You win")
        break
    elif check(6,7,8) == True:
        print("you win")
        break
    elif check(0,3,6) == True:
        print("You win")
        break
    elif check(1,4,7) == True:
        print("you win")
        break
    elif check(2,5,8) == True:
        print("You win")
        break
    elif check(0,4,8) == True:
        print("You win")
        break
    elif check(2,4,6) == True:
        print("You win")
        break
    pygame.display.flip()