import pygame
import random
import os
import sys


def draw_snake_head():
    if x1_change == 0 and y1_change == 0:
        sprite1.rect.x = x1 - 1
        sprite1.rect.y = y1 - 1
        draw_snake()
        all_sprites1.draw(screen)
    elif x1_change == - 3:
        sprite4.rect.x = x1 - 1
        sprite4.rect.y = y1 - 1
        body.rect = sprite4.image.get_rect()
        draw_snake()
        all_sprites4.draw(screen)
    elif x1_change == + 3:
        sprite3.rect.x = x1 - 1
        sprite3.rect.y = y1 - 1
        body.rect = sprite3.image.get_rect()
        draw_snake()
        all_sprites3.draw(screen)
    elif y1_change == + 3:
        sprite2.rect.x = x1 - 1
        sprite2.rect.y = y1 - 1
        body.rect = sprite2.image.get_rect()
        draw_snake()
        all_sprites2.draw(screen)
    elif y1_change == - 3:
        sprite1.rect.x = x1 - 1
        sprite1.rect.y = y1 - 1
        body.rect = sprite1.image.get_rect()
        draw_snake()
        all_sprites1.draw(screen)


def print_score():
    text = font.render("Ваши очки " + str(score), True, (150, 0, 100))
    text_x = 30
    text_y = 30
    screen.blit(text, (text_x, text_y))


def snake_load_image(name, colorkey=-1):
    fullname = os.path.join("../snake/data", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (32, 32))
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def wall_load_image(name, colorkey=None):
    fullname = os.path.join("../snake/data", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (30, 30))
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def draw_walls():
    all_walls = pygame.sprite.Group()
    sprite_wall = pygame.sprite.Sprite()
    sprite_wall.image = wall_load_image("Wall.jpg")
    all_walls.add(sprite_wall)
    sprite_wall.rect = sprite_wall.image.get_rect()
    sprite_wall.rect.x = wall_x
    sprite_wall.rect.y = wall_y
    all_walls.draw(screen2)
    for j in range(16):
        sprite_wall.rect.x = sprite_wall.rect.x + 30
        all_walls.draw(screen2)
    for j in range(16):
        sprite_wall.rect.y = sprite_wall.rect.y + 30
        all_walls.draw(screen2)
    for j in range(16):
        sprite_wall.rect.x = sprite_wall.rect.x - 30
        all_walls.draw(screen2)
    for j in range(15):
        sprite_wall.rect.y = sprite_wall.rect.y - 30
        all_walls.draw(screen2)
    screen.blit(screen2, (0, 0))
    pygame.display.flip()


def draw_snake():
    for j in snake_body:
        body.rect.x = j[0]
        body.rect.y = j[1]
        all_body.draw(screen)


x1 = 240
y1 = 240
button_x = 210
button_y = 235
wall_x = 0
wall_y = 0
x1_change = 0
y1_change = 0
dis_width = 495
dis_height = 495
position_change = 30
score = 0
direction = 0
eaten_fruits = 0
snake_body = []
x2, y2 = x1, y1
past_position = []
game_over = False
game_close = True
press_x, press_y = 0, 0
games_played = 0

pygame.init()
size = width, height = 510, 510
screen = pygame.display.set_mode(size)
screen2 = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')

draw_walls()

cherry_x = round(random.randrange(30, dis_width - 30) / 30.0) * 30.0
cherry_y = round(random.randrange(30, dis_height - 30) / 30.0) * 30.0

apple_x = round(random.randrange(30, dis_width - 30) / 30.0) * 30.0
apple_y = round(random.randrange(30, dis_height - 30) / 30.0) * 30.0

# Раздел с полной прогрузкой всех спрайтов и их дополнение в группы
# Голова вверх
all_sprites1 = pygame.sprite.Group()
sprite1 = pygame.sprite.Sprite()
sprite1.image = snake_load_image("Snake_head_1.jpg")
all_sprites1.add(sprite1)
sprite1.rect = sprite1.image.get_rect()
# Голова вниз
all_sprites2 = pygame.sprite.Group()
sprite2 = pygame.sprite.Sprite()
sprite2.image = snake_load_image("Snake_head_2.jpg")
all_sprites2.add(sprite2)
sprite2.rect = sprite2.image.get_rect()
# Голова влево
all_sprites4 = pygame.sprite.Group()
sprite4 = pygame.sprite.Sprite()
sprite4.image = snake_load_image("Snake_head_4.jpg")
all_sprites4.add(sprite4)
sprite4.rect = sprite4.image.get_rect()
# Голова вправо
all_sprites3 = pygame.sprite.Group()
sprite3 = pygame.sprite.Sprite()
sprite3.image = snake_load_image("Snake_head_3.jpg")
all_sprites3.add(sprite3)
sprite3.rect = sprite3.image.get_rect()
# Фрукты
all_sprites_fruit = pygame.sprite.Group()

all_sprites_fruit2 = pygame.sprite.Group()
sprite_fruit = pygame.sprite.Sprite()
sprite_fruit.image = snake_load_image("Fruit_1.jpg")
all_sprites_fruit.add(sprite_fruit)
sprite_fruit.rect = sprite_fruit.image.get_rect()
apple = pygame.sprite.Sprite()
apple.image = snake_load_image("Fruit_2.jpg")
all_sprites_fruit2.add(apple)
apple.rect = apple.image.get_rect()
# для очков, создание фона
font = pygame.font.Font(None, 30)

all_body = pygame.sprite.Group()
body = pygame.sprite.Sprite()
body.image = snake_load_image("Body_3.jpg")
body.rect = body.image.get_rect()
all_body.add(body)

clock = pygame.time.Clock()
while not game_over:
    if game_close:
        x1 = 240
        y1 = 30
        x1_change = -3
        y1_change = 0
        eaten_fruits = 0
        press_x, press_y = 0, 0
        for i in range(len(snake_body)):
            del snake_body[0]
        draw_walls()
    while game_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = False
                game_over = True
            if event.type == pygame.MOUSEMOTION:
                press_x, press_y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                press_x, press_y = event.pos
                print(event.pos)
                if button_x <= press_x <= button_x + 90 and button_y <= press_y <= button_y + 40:
                    game_close = False
                    score = 0
                    eaten_fruits = 0
                    for i in range(len(snake_body)):
                        del snake_body[0]
                    direction = 0
                    x1_change = 0
                    y1_change = 0
                    x1 = 240
                    y1 = 240

        screen.fill("black", (30, 30, dis_height - 45, dis_width - 45))
        pygame.draw.rect(screen, (255, 255, 0), (30, 30, dis_height - 45, dis_width - 45), 1)
        pygame.draw.rect(screen, (0, 200, 150), (button_x, button_y, 90, 40))
        if button_x <= press_x <= button_x + 90 and button_y <= press_y <= button_y + 40:
            pygame.draw.rect(screen, (0, 100, 150), (button_x, button_y, 90, 40))
        if games_played >= 1:
            # отрисовка надписи (Вы проиграли, выши очки ...)
            text = font.render("Вы проиграли!", True, (150, 0, 100))
            text_x = 182
            text_y = 80
            screen.blit(text, (text_x, text_y))
            text = font.render("Заработан очков: " + str(score), True, (150, 0, 100))
            text_x = 150
            text_y = 110
            screen.blit(text, (text_x, text_y))
            text = font.render("Рестарт", True, (150, 0, 10))
            text_x = 218
            text_y = 245
            screen.blit(text, (text_x, text_y))
        if games_played == 0:
            text = font.render("Cтарт", True, (150, 0, 10))
            text_x = 226
            text_y = 245
            screen.blit(text, (text_x, text_y))
        # отрисовка змеи в меню
        if x1 == 450 and y1 == 30:
            x1_change = -3
            y1_change = 0
        elif x1 == 30 and y1 == 30:
            x1_change = 0
            y1_change = 3
        elif x1 == 30 and y1 == 450:
            x1_change = 3
            y1_change = 0
        elif x1 == 450 and y1 == 450:
            x1_change = 0
            y1_change = -3

        draw_snake_head()

        x2, y2 = x1 - 1, y1 - 1
        x1 += x1_change
        y1 += y1_change
        snake_Head = [x2, y2]
        snake_body.append(snake_Head)
        pygame.display.flip()
        eaten_fruits = 10
        if len(snake_body) > eaten_fruits * 10:
            del snake_body[0]
        if not game_close:
            eaten_fruits = 0

        clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1
                if x1 % 30 == 0 and y1 % 30 == 0:
                    x1_change = -3
                    y1_change = 0
            elif event.key == pygame.K_RIGHT:
                direction = 2
                if x1 % 30 == 0 and y1 % 30 == 0:
                    x1_change = 3
                    y1_change = 0
            elif event.key == pygame.K_UP:
                direction = 3
                if x1 % 30 == 0 and y1 % 30 == 0:
                    x1_change = 0
                    y1_change = -3
            elif event.key == pygame.K_DOWN:
                direction = 4
                if x1 % 30 == 0 and y1 % 30 == 0:
                    x1_change = 0
                    y1_change = 3
    if x1 >= dis_width - 40 or x1 < 30 or y1 >= dis_height - 40 or y1 < 30:
        game_close = True
        games_played += 1

    if direction == 1 and x1 % 30 == 0 and y1 % 30 == 0:
        x1_change = -3
        y1_change = 0
    elif direction == 2 and x1 % 30 == 0 and y1 % 30 == 0:
        x1_change = 3
        y1_change = 0
    elif direction == 3 and x1 % 30 == 0 and y1 % 30 == 0:
        x1_change = 0
        y1_change = -3
    elif direction == 4 and x1 % 30 == 0 and y1 % 30 == 0:
        x1_change = 0
        y1_change = 3

    print(x1, y1, x1_change, y1_change, len(snake_body))
    x2, y2 = x1 - 1, y1 - 1
    x1 += x1_change
    y1 += y1_change
    snake_Head = [x2, y2]
    snake_body.append(snake_Head)
    if len(snake_body) > eaten_fruits * 10:
        del snake_body[0]

    screen.fill("black", (30, 30, dis_height - 45, dis_width - 45))

    draw_snake_head()

    # Отрисовка вишенки
    sprite_fruit.rect.x = cherry_x
    sprite_fruit.rect.y = cherry_y
    all_sprites_fruit.draw(screen)

    if x1 == cherry_x and y1 == cherry_y:
        cherry_x = round(random.randrange(30, dis_width - 30) / 30.0) * 30.0
        cherry_y = round(random.randrange(30, dis_height - 30) / 30.0) * 30.0
        score += 1
        eaten_fruits += 1

    if score > 1 and score % 15 == 0:
        apple.rect.x = apple_x
        apple.rect.y = apple_y
        all_sprites_fruit2.draw(screen)
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(30, dis_width - 30) / 30.0) * 30.0
            apple_y = round(random.randrange(30, dis_height - 30) / 30.0) * 30.0
            score += 5
            eaten_fruits += 1

    pygame.draw.rect(screen, (255, 255, 0), (30, 30, dis_height - 45, dis_width - 45), 1)

    print_score()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
