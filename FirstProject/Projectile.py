import pygame

screenHeight, screenWidth = 800, 600


class Bullet(object):
    def __init__(self, x, y, dir, r):
        self.x = x
        self.y = y
        self.dir = dir
        self.r = r
        self.hitbox = pygame.Rect(x - r, y - r, r * 2, r * 2)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (255, 255, 255),
                           (int(self.x), int(self.y)),
                           self.r)
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 1)

    def move(self):
        if self.dir == "right":
            self.x += 0.2
            self.hitbox.x = self.x - self.r

        elif self.dir == "left":
            self.x -= 0.2
            self.hitbox.x = self.x - self.r

        elif self.dir == "up":
            self.y -= 0.2
            self.hitbox.y = self.y - self.r

        elif self.dir == "down":
            self.y += 0.2
            self.hitbox.y = self.y - self.r

    def isOffScreen(self):
        #off right
        if self.x > pygame.display.get_surface().get_width():
            return True
        #off left
        if self.x < 0-(2*self.r):
            return True
        #offbottom
        if self.y > pygame.display.get_surface().get_height():
            return True
        #off top
        if self.y < (0-2*self.r):
            return True
        else:
            return False

    def isColliding(self,otherRect):
        if self.hitbox.colliderect(otherRect):
            return True
        else:
            return False

