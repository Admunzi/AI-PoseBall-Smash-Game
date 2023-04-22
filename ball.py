import pygame
import random


class Ball:
    def __init__(self, screen, speed):
        self.screen_width = screen[0]
        self.screen_height = screen[1]
        self.radius = 20
        self.color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.x = random.randint(self.radius, self.screen_width - self.radius * 2)
        self.y = random.randint(self.radius, self.screen_height - self.radius * 2)

        # DY and DX are the speed of the ball, aleatory front or back
        self.dy = random.choice([-speed, speed])
        self.dx = random.choice([-speed, speed])

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < 0 or self.x > self.screen_width - self.radius * 2:
            self.dx *= -1
        if self.y < 0 or self.y > self.screen_height - self.radius * 2:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_collision(self, landmark_list):
        if landmark_list is not None:
            for landmark in landmark_list.landmark:
                x, y = int(landmark.x * self.screen_width), int(landmark.y * self.screen_height)
                if self.x - self.radius < x < self.x + self.radius and self.y - self.radius < y < self.y + self.radius:
                    return True
        return False
