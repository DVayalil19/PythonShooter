import pygame
import Projectile

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 30)
done = False
gameState = "playing"
screenHeight, screenWidth = 800, 600

player1 = pygame.image.load("smallCharacter.png")
p1X, p1Y = 100, 100
p1HitBox = player1.get_rect()
p1Bullets = []
p1Dir = "right"
p1Health = 100

player2 = pygame.image.load("smallCharacter2.png")
p2X, p2Y = 400, 400
p2HitBox = player2.get_rect()
p2Bullets = []
p2Dir = "right"
p2Health = 100
size = 20

while not done:
    # check for keypress
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if gameState == "playing":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                p1Bullets.append(Projectile.Bullet(p1X + 2.5, p1Y + 2.50, p1Dir, 5))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                p2Bullets.append(Projectile.Bullet(p2X + 2.5, p2Y + 2.50, p2Dir, 5))
        if gameState == "GameOver":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                p1X, p1Y = 100, 100
                p1Bullets = []
                p1Dir = ""
                p1Health = 100

                p2X, p2Y = 400, 400
                p2Bullets = []
                p2Dir = ""
                p2Health = 100
                gameState = "playing"

    if gameState == "playing":
        # check for keypress continually
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            p1X += 0.15
            p1Dir = "right"
        if pressed[pygame.K_LEFT]:
            p1X -= 0.15
            p1Dir = "left"
        if pressed[pygame.K_UP]:
            p1Y -= 0.15
        if pressed[pygame.K_DOWN]:
            p1Y += 0.15

        if pressed[pygame.K_d]:
            p2X += 0.15
            p2Dir = "right"
        if pressed[pygame.K_a]:
            p2X -= 0.15
            p2Dir = "left"
        if pressed[pygame.K_w]:
            p2Y -= 0.15
        if pressed[pygame.K_s]:
            p2Y += 0.15

        if p1X > 800 + size:
            p1X = 0 - size
        if p1X < 0 - size:
            p1X = 800 + size
        if p1Y > 600 + size:
            p1Y = 0 - size
        if p1Y < 0 - size:
            p1Y = 600 + size

        if p2X > 800 + size:
            p2X = 0 - size
        if p2X < 0 - size:
            p2X = 800 + size
        if p2Y > 600 + size:
            p2Y = 0 - size
        if p2Y < 0 - size:
            p2Y = 600 + size

        # update hitbox
        p1HitBox.x = p1X
        p1HitBox.y = p1Y

        p2HitBox.x = p2X
        p2HitBox.y = p2Y

        if p1HitBox.colliderect(p2HitBox):
            p1HitBox.x, p1HitBox.y = 10, 10
            p1X, p1Y = 10, 10

            # move the bullets
        for b in p1Bullets:
            b.move()
            if b.isOffScreen():
                p1Bullets.remove(b)
            if b.isColliding(p2HitBox):
                p1Bullets.remove(b)
                p2Health -= 10
                if p2Health <= 0:
                    p2Health = 0
                    gameState = "GameOver"

        for b in p2Bullets:
            b.move()
            if b.isOffScreen():
                p2Bullets.remove(b)
            if b.isColliding(p1HitBox):
                p2Bullets.remove(b)
                p1Health -= 10
                if p1Health <= 0:
                    p1Health = 0
                    gameState = "GameOver"


        # draw all the graphics
        screen.fill((118, 85, 43))

        # Health Bars
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, p1Health, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(600, 10, p2Health, 10))

        # draw text
        textSurface = myFont.render("Bullet: " + str(len(p1Bullets)), False, (255, 255, 255))
        screen.blit(textSurface, (0, 0))

        # draw Bullet
        for b in p1Bullets:
            b.draw(screen)
        for b in p2Bullets:
            b.draw(screen)

        # draw hitbox
        pygame.draw.rect(screen, (255, 0, 0), p1HitBox, 1)
        pygame.draw.rect(screen, (255, 0, 0), p2HitBox, 1)

        # draw character
        if p2Dir == "right":
            screen.blit(pygame.transform.flip(player2, True, False), (p2X, p2Y))
        else:
            screen.blit(player2, (p2X, p2Y))
        if p1Dir == "right":
            screen.blit(pygame.transform.flip(player1, True, False), (p1X, p1Y))
        else:
            screen.blit(player1, (p1X, p1Y))

    if gameState == "GameOver":
        if p1Health<=0 and p2Health <= 0:
            textSurface = myFont.render("Tie Game!!!", False, (255, 255, 255))
            screen.blit(textSurface, (400, 300))
        if p1Health<=0:
            textSurface = myFont.render("Player 2 Wins", False, (255, 255, 255))
            screen.blit(textSurface, (400, 300))
        if p2Health<=0:
            textSurface = myFont.render("Player 1 Wins", False, (255, 255, 255))
            screen.blit(textSurface, (400, 300))


    # Needs to be the LAST LINE
    pygame.display.flip()
