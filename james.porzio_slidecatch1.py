# import necessary modules like pygame, simpleGE, and random
import pygame, random, simpleGE
# define class for falling gold
class Gold(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
# set image for gold
        self.setImage("Gold.png")
# scale sprite correctly
        self.setSize(31, 31)
# reset sprite position
        self.reset()
        
    def reset(self):
# gold starts falling from sky
        self.y = 11
# random integer for x 
        self.x = random.randint(0, self.screenWidth)
# random integer for y speed
        self.dy = random.randint(4, 6)
        
    def checkBounds(self):
# reset when gold is off screen
        if self.bottom > self.screenHeight:
            self.reset()
# define new class for the robot character
class Robot(simpleGE.Sprite):
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
    
    def process(self):
# move robot left if left arrow key is pressed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
# move robot right if right arrow key is pressed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
       
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("backgg.png")
        
        self.sndGold = simpleGE.Sound("my_original_sound.wav")
        
        self.robot = Robot(self)
        self.numGolds = 4
        self.golds = []
        for i in range(self.numGolds):
            self.golds.append(Gold(self))
        
        self.sprites = [self.robot,
                        self.golds]
        
    def process(self):
        for gold in self.golds:
            if self.robot.collidesWith(gold):
                self.sndGold.play()
                gold.reset()
    
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()