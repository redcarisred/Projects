# I wrote this computer code for a pygame game in Python
import os
import random
import pygame
import time
import math
# Classes for players and enemies
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
class Cat5(object):
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.speed = 2
    def move(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.x -= dx*self.speed
        self.y -= dy*self.speed
    def bounce(self, cats):
        for player in cats:
            if player != cats[4]:
                dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
                dist = math.hypot(dx, dy)
                if dist < 10: 
                    if dist != 0:
                        dx, dy = dx / dist, dy / dist
                    # move along this normalized vector towards the player at current speed
                    self.rect.x += dx * self.speed
                    self.rect.y += dy * self.speed
                    self.x += dx*self.speed
                    self.y += dy*self.speed
class Cat(object):
    def __init__(self):
        self.x = 300
        self.y = 300
        self.speed = 1
    def move(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.x -= dx*self.speed
        self.y -= dy*self.speed
    def bounce(self, cats):

        for player in cats:
            if player != cats[0]:
                dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
                dist = math.hypot(dx, dy)
                if dist < 10: 
                    if dist != 0:
                        dx, dy = dx / dist, dy / dist
                    # move along this normalized vector towards the player at current speed
                    self.rect.x += dx * self.speed
                    self.rect.y += dy * self.speed
                    self.x += dx*self.speed
                    self.y += dy*self.speed
class Cat2(object):
    def __init__(self):
        self.x = 0
        self.y = 350
        self.speed = 1.25
    def move(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.x -= dx*self.speed
        self.y -= dy*self.speed
    def bounce(self, cats):

        for player in cats:
            if player != cats[1]:
                dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
                dist = math.hypot(dx, dy)
                if dist < 10: 
                    if dist != 0:
                        dx, dy = dx / dist, dy / dist
                    # move along this normalized vector towards the player at current speed
                    self.rect.x += dx * self.speed
                    self.rect.y += dy * self.speed
                    self.x += dx*self.speed
                    self.y += dy*self.speed
class Cat3(object):
    def __init__(self):
        self.x = 650 
        self.y = 400
        self.speed = 1.5
    def move(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.x -= dx*self.speed
        self.y -= dy*self.speed
    def bounce(self, cats):

        for player in cats:
            if player != cats[2]:
                dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
                dist = math.hypot(dx, dy)
                if dist < 10: 
                    if dist != 0:
                        dx, dy = dx / dist, dy / dist
                    # move along this normalized vector towards the player at current speed
                    self.rect.x += dx * self.speed
                    self.rect.y += dy * self.speed
                    self.x += dx*self.speed
                    self.y += dy*self.speed
class Cat4(object):
    def __init__(self):
        self.x = 450
        self.y = 450
        self.speed = 1.75
    def move(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.x -= dx*self.speed
        self.y -= dy*self.speed
    def bounce(self, cats):

        for player in cats:
            if player != cats[3]:
                dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
                dist = math.hypot(dx, dy)
                if dist < 10: 
                    if dist != 0:
                        dx, dy = dx / dist, dy / dist
                    # move along this normalized vector towards the player at current speed
                    self.rect.x += dx * self.speed
                    self.rect.y += dy * self.speed
                    self.x += dx*self.speed
                    self.y += dy*self.speed

class Stone(object):
    def __init__(self):
        self.x = 580
        self.y = 470
        self.rect = pygame.Rect(self.x,self.y,16,16)
class Stone2(object):
    def __init__(self):
        self.x = 40
        self.y = 460
        self.rect = pygame.Rect(self.x,self.y,16,16)
# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
# Set up the start screen
pygame.display.set_caption("Escape!")
screen = pygame.display.set_mode((700, 490))
clock = pygame.time.Clock()
q = False
do = False
while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = True
            do = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                q = True
                do = True
            elif event.key == pygame.K_s:
                do = True
    screen.fill((0,0,255))
    font = pygame.font.SysFont('Algerian',50,True,False)
    text = font.render('ESCAPE!',True,(255,0,0))
    screen.blit(text,[200,70])
    font = pygame.font.SysFont('Times New Roman',30,True,False)
    text = font.render('Arrow keys to move.',True,(255,165,0))
    screen.blit(text,[200,200])
    text = font.render('Get to the green circle!',True,(255,255,0))
    screen.blit(text,[200,230])
    text = font.render('Avoid triangles and avoid rocks too!',True,(0,255,0))
    screen.blit(text,[100,260])
    text = font.render("Press 's' to start!",True,(128,0,128))
    screen.blit(text,[220,400])
    pygame.display.flip()
    clock.tick(60)
if q == True:
    running = False
else:
    running = True

# Gameplay
walls = [] # List to hold the walls
player = Player() # Create the player
cat = Cat()
cat2 = None
cat3 = None
cat4 = None
cat5 = None
# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                  WW                  W",
"W                  WW                  W",
"W    WWWW  WWWWWW      WWWWWW  WWWW    W",
"W    WWWW  WWWWWW      WWWWWW  WWWW    W",
"W                                      W",                                 
"W              WWWWWWWWWW              W",
"W  WWWWWW      WWWWWWWWWW      WWWWWW  W",
"W         WW       WW       WW         W",
"W         WW       WW       WW         W",
"W         WWWWWW   WW   WWWWWW         W",
"W         WWWWWWWW    WWWWWWWW         W",
"WWWWWWW   WW                WW   WWWWWWW",
"WWWWWWW   WW    WW    WW    WW   WWWWWWW",
"W               W      W              WWWWWW",
"W               W      W                   W",
"WWWWWWWWWWWWW   WWWWWWWW   WWWWWWWWWWWWW   W",
"WWWWWWWWWWWWW              WWWWWWWWWWWWW   W",
"W          WW              WW          W   W",
"W              WWWWWWWWWW              W   W",
"W                  WW                  W   W",
"W  WWWW     WWWW   WW   WWWW     WWWW  W   W",
"W     W                          W     W   W",
"WW    W    W                W    W    WW   W",
"W          W                W          WWW W",
"WWW WWWWWWWWWWW         WWWWWWWWWWWWW      W",
"WWW WWWWWWWWWWWWWWW WWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                     EW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0
level = 1
canAdd = True
rock = Stone()
rock2 = Stone2()
while running:
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    
    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect) and level == 5:
        won = True
        running = False
    elif player.rect.colliderect(end_rect) and canAdd == True:
        level += 1
        if level == 2:
            cat2 = Cat2()
        elif level == 3:
            cat3 = Cat3()
        elif level == 4:
            cat4 = Cat4()
        elif level == 5:
            cat5 = Cat5()
        canAdd = False
        player.x = 0
        player.y = 0
        player.rect = pygame.Rect(32, 32, 16, 16)
        canAdd = True
    cat.move(player)
    if cat2 != None:
        cat2.move(player)
    if cat3 != None:
        cat3.move(player)
    if cat4 != None:
        cat4.move(player)
    if cat5 != None:
        cat5.move(player)
    if player.rect.colliderect(cat.rect):
        won = False
        running = False
    if cat2 != None:
        if player.rect.colliderect(cat2.rect):
            won = False
            running = False
    if cat3 != None:
        if player.rect.colliderect(cat3.rect):
            won = False
            running = False
    if cat4 != None:
        if player.rect.colliderect(cat4.rect):
            won = False
            running = False
    if cat5 != None:
        if player.rect.colliderect(cat5.rect):
            won = False
            running = False
    if player.rect.colliderect(rock.rect):
        won = False
        running = False
    if player.rect.colliderect(rock2.rect):
        won = False
        running = False
    cats = [cat]
    if cat2 != None:
        cats.append(cat2)
    if cat3 != None:
        cats.append(cat3)
    if cat4 != None:
        cats.append(cat4)
    if cat5 != None:
        cats.append(cat5)
    cat.bounce(cats)
    if cat2 != None:
        cat2.bounce(cats)
    if cat3 != None:
        cat3.bounce(cats)      
    if cat4 != None:
        cat4.bounce(cats)  
    if cat5 != None:
        cat5.bounce(cats)            
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (0,0, 255), wall.rect)

    
    pygame.draw.circle(screen, (0, 255, 0), (end_rect[0],end_rect[1]),16)
    pygame.draw.circle(screen,(255,0,0),(rock.x,rock.y),8)
    pygame.draw.circle(screen,(255,0,0),(rock2.x,rock2.y),8)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.draw.polygon(screen,(255,0,0),((cat.x,cat.y+30),(cat.x+30,cat.y),(cat.x+30,cat.y+30)))
    if cat2 != None:
        pygame.draw.polygon(screen,(255,165,0),((cat2.x,cat2.y+30),(cat2.x+30,cat2.y),(cat2.x+30,cat2.y+30)))
    if cat3 != None:
        pygame.draw.polygon(screen,(255,255,0),((cat3.x,cat3.y+30),(cat3.x+30,cat3.y),(cat3.x+30,cat3.y+30)))
    if cat4 != None:
        pygame.draw.polygon(screen,(0,255,0),((cat4.x,cat4.y+30),(cat4.x+30,cat4.y),(cat4.x+30,cat4.y+30)))
    if cat5 != None:
        pygame.draw.polygon(screen,(128,0,128),((cat5.x,cat5.y+30),(cat5.x+30,cat5.y),(cat5.x+30,cat5.y+30)))
    

    rock.x -= level
    rock2.x += level
    rock.rect = pygame.Rect(rock.x,rock.y,16,16)
    rock2.rect = pygame.Rect(rock2.x,rock2.y,16,16)
    if rock.x < 40:
        rock.x = 580 
    if rock2.x > 580:
        rock2.x = 40
    font = pygame.font.SysFont('Times New Roman',25,True,False)
    font = pygame.font.SysFont('Times New Roman',25,True,False)
    text = font.render('Level: '+str(level),True,(255,255,0))
    screen.blit(text,[20, 460])
    pygame.display.flip()

screen.fill((255,255,255))
font = pygame.font.SysFont('Times New Roman',50,True,False)
try:
    if won == True:
        pass
except:
    print('You quit the game.')
else:
    if won == True:
        text = font.render('You win!',True,(0,0,0))
        screen.blit(text,[170,200])
        screen.blit((font.render('Yay! You finished the game!',True,(0,0,0))),[0,400])
    elif won == False:
        text = font.render('You lost! You died in level '+str(level),True,(0,0,0))
        screen.blit(text,[50,200])
        if level == 1:
            screen.blit((font.render('Come on! Beaten in Level ONE???',True,(0,0,0))),[0,400])
        if level == 2:
            screen.blit((font.render('You could do better.',True,(0,0,0))),[0,400])
        if level == 3:
            screen.blit((font.render('Good job!',True,(0,0,0))),[0,400])
        if level == 4:
            screen.blit((font.render('Wow! You did very well!',True,(0,0,0))),[0,400])
        if level == 5:
            screen.blit((font.render('Wow! Can you escape from the large purple triangle?',True,(0,0,0))),[0,400])
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
