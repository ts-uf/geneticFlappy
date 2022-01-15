import pygame as pg
from Wall import Wall
from Bird import Bird
from constants import *
from time import sleep
from Neuron import Neuron
from random import uniform


def draw_wall():
    for wall in walls_on_map:
        pg.draw.rect(screen, BLUE, [wall.placeX, 0, WALLTHCKNESS, wall.gapY])
        placeY = wall.gapY + WALLGAP
        pg.draw.rect(screen, BLUE, [wall.placeX, placeY, WALLTHCKNESS, SIZEY - placeY])


def move_walls():
    for wall in walls_on_map:
        wall.move_wall()

def move_birds():
    for bird in birds:
        bird.move_bird()
        bird.score += 1


def draw_birds():
    for bird in birds:
        screen.blit(image, (BIRDX, bird.placeY))
    # pg.draw.rect(screen, RED, [BIRDX, bird.placeY, BIRDSIZE, BIRDSIZE], 0)

def spawn_birds():
    for i in range(100):
        birds.append(Bird())


def check_jump():
    for bird in birds:
        bird.brain.inputs[0].value = bird.speed
        bird.brain.inputs[1].value = bird.placeY
        bird.brain.inputs[2].value = walls_on_map[0].placeX
        bird.brain.inputs[3].value = walls_on_map[0].gapY
        bird.brain.calculate()
        print(bird.brain.output)
        if not bird.brain.output > 0:
            bird.jump()

def mutate_birds(bird, num):
    for i in range(int(num/2)):
        Mbird = Bird()
        Mbird.cpy(bird)
        var = uniform(-0.1, 0)
        # print(var)
        Mbird.brain.mutate(var)
        birds.append(Mbird)
        Mbird = Bird()
        Mbird.cpy(bird)
        var = uniform(0, 0.1)
        # print(var)
        Mbird.brain.mutate(var)
        birds.append(Mbird)


if __name__ == '__main__':
    birds = []
    walls_on_map = []
    wall_countdown = 0
    walls_passed = 0
    bird_die_countdown = 100
    gen = 0
    dead_birds = []

    pg.init()

    image = pg.image.load(".\\Images\\hape_head.png")
    image = pg.transform.scale(image, (BIRDSIZE + 5, BIRDSIZE + 5))

    # creating new window
    size = (SIZEX, SIZEY)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Flappy Genetic Code")

    while True:
        birds = []
        walls_on_map = []
        wall_countdown = 0
        walls_passed = 0
        bird_die_countdown = 100
        gen += 1
        run = True

        # creating birds
        if len(dead_birds) == 0:
            spawn_birds()
        else:
            """
            10 random birds
            5 same as top 5
            36 based on 1st
            22 based on 2nd
            14 based on 3rd
            8 based on 4th
            4 based on 5th
            """
            dead_birds = sorted(dead_birds, key=lambda x: x.score, reverse=True)

            for i in range(5):
                birds.append(Bird())
            for i in range(5):
                dead_birds[i].score = 0
                birds.append(dead_birds[i])
            mutate_birds(dead_birds[0], 38)
            mutate_birds(dead_birds[1], 24)
            mutate_birds(dead_birds[2], 14)
            mutate_birds(dead_birds[3], 10)
            mutate_birds(dead_birds[4], 4)

        dead_birds = []

        while run:

            # checking for game events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            if wall_countdown == 0:
                walls_on_map.append(Wall())
                wall_countdown = GAPBETWEENWALLS

            check_jump()

            # dead checks
            # boder checks
            for bird in birds:
                if not 0 < bird.placeY < SIZEY:
                    bird_die_countdown -= 1
                    dead_birds.append(bird)
                    birds.remove(bird)

                # wall checks
                else:
                    for wall in walls_on_map:
                        if wall.placeX + WALLTHCKNESS > BIRDX and wall.placeX < BIRDX + BIRDSIZE:  # BIRDSIZE is only to the right
                            if wall.gapY > bird.placeY or bird.placeY + BIRDSIZE > wall.gapY + WALLGAP:  # BIRDSIZE is only to the left
                                bird_die_countdown -= 1
                                dead_birds.append(bird)
                                birds.remove(bird)

            # game logic
            screen.fill(WHITE)  # cleaning the screen

            # wall logic
            for wall in walls_on_map:
                if wall.placeX + 50 < BIRDX:
                    walls_on_map.remove(wall)
                    walls_passed += 1
                    print(walls_passed)

            if wall_countdown == 0:
                walls_on_map.append(Wall())
                wall_countdown = GAPBETWEENWALLS

            draw_birds()
            draw_wall()

            #  update the screen
            pg.display.flip()

            # update game tools
            move_birds()
            move_walls()
            wall_countdown -= 1

            #  delay between loops
            sleep(0.05)

            #
            if bird_die_countdown <= 0:
                run = False

        print(f'gen: {gen}, your score was: {walls_passed}')





