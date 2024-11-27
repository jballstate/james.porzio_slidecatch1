# import necessary modules like pygame, simpleGE, and random
import pygame, random, simpleGE
# define class for falling gold
class Gold(simpleGE.Sprite):
# initialize gold
    def __init__(self, scene):
        super().__init__(scene)
# set image for gold
        self.setImage("Gold.png")
# scale sprite correctly
        self.setSize(31, 31)
# reset sprite position
        self.reset()
# method to reset gold      
    def reset(self):
# gold starts falling from sky
        self.y = 11
# random integer for x 
        self.x = random.randint(0, self.screenWidth)
# random integer for y speed
        self.dy = random.randint(4, 6)
# method to check if gold is off screen       
    def checkBounds(self):
# reset when gold is off screen
        if self.bottom > self.screenHeight:
            self.reset()
# define new class for the robot character
class Robot(simpleGE.Sprite):
# initialize robot
    def __init__(self, scene):
        super().__init__(scene)
# set image for robot
        self.setImage("robot.png")
# scale sprite correctly
        self.setSize(65, 65)
# robot starts on the ground
        self.position = (300, 450)
# robot move speed
        self.moveSpeed = 3
# method for movement
    def process(self):
# move robot left if left arrow key is pressed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
# move robot right if right arrow key is pressed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
# define class for game
class Game(simpleGE.Scene):
# initialize game
    def __init__(self):
        super().__init__()
# set image for background
        self.setImage("backgg.png")
# set sound for collision 
        self.sndGold = simpleGE.Sound("my_original_sound.wav")
# create robot
        self.robot = Robot(self)
# amount of gold
        self.numGolds = 4
# create gold
        self.golds = []
        for i in range(self.numGolds):
            self.golds.append(Gold(self))
# add robot and gold sprite to scene
        self.sprites = [self.robot,
                        self.golds]
# method for collision
    def process(self):
        for gold in self.golds:
# robot gold collision
            if self.robot.collidesWith(gold):
# play my original sound
                self.sndGold.play()
# reset gold
                gold.reset()
# define new function for main
def main():
# run game class
    game = Game()
# start game
    game.start()
# if name is main, call main function to start game
if __name__ == "__main__":
    main()