import pygame
from pygame.locals import *
import pygbutton
from sys import exit
import random
from time import sleep
import serial

class Mark:
    def __init__(self, theImage, x, y):
        self.markimage = theImage
        self.x = x
        self.y = y
        self.shape = pygame.image.load(theImage)
    
    def Show(self, surface):
        surface.blit(self.shape, (self.x, self.y))

class Chessboard:
    def __init__(self, theImage, x, y):
        self.boardimage = theImage
        self.x = x
        self.y = y
        self.shape = pygame.image.load(theImage)
    
    def Show(self, surface):
        surface.blit(self.shape, (self.x, self.y))


def main():
    pygame.init()
    pygame.display.set_caption("roboChess") #title bar
    board_image = 'chessboard.jpg'
    surface_board = Chessboard(board_image, 0, 0)
    #windowsize = (900,800)
    windowsize = (800,800)
    surfacecolor = (236,123,14) ################
    grip_close_button = pygbutton.PygButton((810,400,80,30), 'grip close')

    screen = pygame.display.set_mode(windowsize, DOUBLEBUF)

    # Uncomment the framerate line and change
    # time = clock.tick() in main loop to
    # to limit the animation to a specific framerate
    #framerate = 50


    #
    # Main loop
    #

    arduino_ttl = serial.Serial('COM3', 9600) #arduino input port
    while True:
        #baseX, baseY = 32, 27 #initial estimation
        baseX, baseY = 50, 55
        screen.fill(surfacecolor)
        surface_board.Show(screen)
        grip_close_button.draw(screen)
        pygame.display.update()
        clicked = 0
        while clicked != 2:
            borderX, borderY, square_posX, square_posY = 112, 105, 0, 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    arduino_ttl.close()
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked += 1
                    click_pos = pygame.mouse.get_pos()
                    #where clicked
                    if click_pos[0] < 770:
                        for col in range(8):
                            if click_pos[0] > borderX:
                                borderX += 96
                            else:
                                square_posX = (col * 92) + baseX
                                break
                        for row in range(8):
                            if click_pos[1] > borderY:
                                borderY += 96
                            else:
                                square_posY = (row * 90) + baseY
                                break
                        #arduino_ttl.write( bin((7 - line) * (col+1)) )
                        print row, col
                        #print str( (8 - line) +(7 - col)*8 ) + "\t" + str(bin( (8 - line) +(7 - col)*8 ))
                        arduino_ttl.write( bin( (8 - row) +(col)*8 ) ) 
                    else:
                        clicked = 0
                        screen.fill(surfacecolor)
                        grip_close_button.draw(screen)
                        surface_board.Show(screen)
                        pygame.display.update()
                        continue

###########################################################################
                    print "clicked"
                    print click_pos
                    mark_image = 'square.jpg'
                    mark_surface = Mark(mark_image, square_posX, square_posY)
                    mark_surface.Show(screen)
                    pygame.display.update()
                    sleep(0.25)


if __name__ == "__main__":
    main()
