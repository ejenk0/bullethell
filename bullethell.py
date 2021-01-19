import pygame
import random
import os

screensize = 600

win = pygame.display.set_mode((screensize, screensize))
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 30)

# dirpath = os.path.dirname(os.path.realpath(__file__))
fullsizeimage = pygame.image.load(dirpath  + "/scratch.png")

x = 10
y = 10
size = 60

enemyspeed = 2
enemies = []

powerups = []

health = 5
slomoeffect = 1

# myCharacter = pygame.transform.scale(fullsizeimage, (size, size))

running = True
while running:
    # Fill the window with black
    win.fill((0, 0, 0))
    # Draw our player to the mouse cursor 
    playerrect = pygame.draw.rect(win, (255, 0, 0), (x, y, size, size))
    # win.blit(myCharacter, (x,y))

    # This is our main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                size += 5
                # myCharacter = pygame.transform.scale(fullsizeimage, (size, size))
            if event.key == pygame.K_DOWN:
                size -= 5
                # myCharacter = pygame.transform.scale(fullsizeimage, (size, size))
        
    if random.randint(0, 100) < 25:
        # SPAWN AN ENEMY!
        up = random.randint(0, 1)
        left = random.randint(0, 1)
        enemies.append([random.randint(0, screensize), up*screensize, up, left, 30, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))])
    
    if random.randint(0, 100) < 25:
        # SPAWN AN POWERUP!
        powerupref = {"health":(245, 66, 102), "slomo":(115, 255, 253)}
        powerup = random.choice(["health", "slomo"])
        powerups.append([random.randint(0, screensize), random.randint(0, screensize), 15, powerupref[powerup], powerup])


    for enemy in enemies:
        # IF THE ENEMY IS GOING UP
        if enemy[2]:
            enemy[1] = enemy[1] - (enemyspeed/slomoeffect)
        else:
            enemy[1] = enemy[1] + (enemyspeed/slomoeffect)
        
        # IF THE ENEMY IS GOING LEFT
        if enemy[3]:
            enemy[0] = enemy[0] - (enemyspeed/slomoeffect)
        else:
            enemy[0] = enemy[0] + (enemyspeed/slomoeffect)
        
        # DRAW THE ENEMY
        enemyrect = pygame.draw.rect(win, enemy[5], (enemy[0], enemy[1], enemy[4], enemy[4]))

        if playerrect.colliderect(enemyrect):
            enemies.remove(enemy)
            health -= 1
    
    for powerup in powerups:
        poweruprect = pygame.draw.rect(win, powerup[3], (powerup[0], powerup[1], powerup[2], powerup[2]))
        if playerrect.colliderect(poweruprect):
            powerups.remove(powerup)
            if powerup[4] == "health":
                health += 1
            if powerup[4] == "slomo":
                slomoeffect += 1
            else:
                slomoeffect = 1

    # Get the position of the mouse
    pos = pygame.mouse.get_pos()
    # Set our player coordinates to the mouse position
    x = pos[0] - 0.5 * size
    y = pos[1] - 0.5 * size

    # HANDLE TEXT
    textsurface = myfont.render("Health: "+ str(health), False, (0, 0, 255))
    win.blit(textsurface, (20, 21))

    # Update the screen
    pygame.display.update()

    clock.tick(30)

    if health <= 0:
        running = False