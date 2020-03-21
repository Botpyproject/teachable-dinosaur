import pygame
import random
import cv2
from PIL import Image
import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, Conv2D, Flatten, MaxPool2D, Dropout, MaxPooling2D


class Game:
    pygame.init()
    clock = pygame.time.Clock()
    width = 1024
    height = 500
    black = (0, 0, 0)
    white = (255, 255, 255)
    display = pygame.display.set_mode((width, height))
    gameExit = False
    dino = pygame.image.load('img/dino.png').convert_alpha()
    cactus = pygame.image.load('img/cactus.png').convert_alpha()
    dino_rect = dino.get_rect()
    cactus_rect = cactus.get_rect()
    cactuses = []
    counter = 0
    y = 50
    camera = cv2.VideoCapture(0)
    exit = False
    score = 0

    def __init__(self):
        self.model = self.load_model()
        self.model.load_weights('weights.h5')
        self.intro()

    def intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gameloop()
            self.display.fill(self.white)
            largeText = pygame.font.Font('freesansbold.ttf', 100)
            textSurf = largeText.render("Press SPACE to play", True, self.black)
            textRect = textSurf.get_rect()
            textRect.center = ((self.width / 2), (self.height / 2))
            self.display.blit(textSurf, textRect)
            pygame.display.update()
            self.clock.tick(30)

    def gameloop(self):
        while not self.gameExit:
            self.display.fill(self.white)
            pygame.draw.line(self.display, self.black, (0, self.height - 50), (self.width, self.height - 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
            if self.counter % (random.randrange(100, 110)) == 0:
                from cactus import Cactus
                self.cactuses.append(Cactus())
            for c in self.cactuses:
                c.showCactus()
                c.x -= 15
                if c.x <= -c.rect.width:
                    self.cactuses = self.cactuses[1:]
            pic = self.take_photo()
            result = self.predict(pic)
            if result == 0:
                pass
            else:
                if self.y == 50:
                    self.y += 150
            self.score += 1
            text = pygame.font.Font('freesansbold.ttf', 20)
            textSurf = text.render("Score: " + str(self.score), True, self.black)
            self.display.blit(textSurf, [10, 10])
            self.display.blit(self.dino, [10, self.height - self.y - self.dino_rect.height])
            pygame.display.update()
            if self.y > 50:
                self.y -= 10
            self.clock.tick(30)
            self.counter += 1
        pygame.quit()
        self.camera.release()
        cv2.destroyAllWindows()
        quit()

    def take_photo(self):
        cv2.resizeWindow('image', 300, 350)
        return_value, image = self.camera.read()
        cv2.imshow('image', image)
        im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(im)
        im = im.resize((100, 100))
        im = np.array(im)
        im = np.resize(im, (1, 100, 100, 3))
        im = (im.astype(float) - 128) / 128
        return im

    def freeze_model(self, model):
        for layer in model.layers:
            layer.trainable = False

    def load_model(self):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1), activation='relu', input_shape=(100, 100, 3)))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Flatten())
        model.add(Dense(1000, activation='sigmoid'))
        model.add(Dropout(0.4))
        model.add(Dense(2, activation='sigmoid'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def predict(self, pic):
        prob = self.model.predict(pic)
        result = np.argmax(prob)
        return result


if __name__ == '__main__':
    g = Game()
