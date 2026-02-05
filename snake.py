import pygame
import random
import sys

# Инициализация PyGame
pygame.init()

# Размеры игры
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Цвета
BACKGROUND = (15, 20, 30)
GRID_COLOR = (40, 50, 70)
SNAKE_HEAD = (50, 255, 100)
SNAKE_BODY = (30, 180, 80)
FOOD_COLOR = (255, 80, 80)
TEXT_COLOR = (255, 255, 255)
GAME_OVER_BG = (0, 0, 0, 180)

# Глобальные переменные
screen = None
clock = None
snake = []
food = (0, 0)
direction = (1, 0)
score = 0
game_over = False
speed = 10
pending_growth = 2

def init_game():
    global screen, clock, snake, food, direction, score, game_over, speed, pending_growth
    
    # Создаем поверхность для рисования
    screen = pygame.Surface((WIDTH, HEIGHT))
    
    # Инициализация змейки
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
    score = 0
    game_over = False
    speed = 10
    pending_growth = 2
    
    # Создаем первую еду
    generate_food()
    
    # Обновляем статистику
    update_stats(score, len(snake), speed)

def generate_food():
    global food
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), 
                random.randint(0, GRID_HEIGHT - 1))
        if food not in snake:
            break

def handle_keys():
    global direction, game_over
    
    keys = get_keys()
    
    for key in keys:
        if key == 'UP' and direction != (0, 1):
            direction = (0, -1)
        elif key == 'DOWN' and direction != (0, -1):
            direction = (0, 1)
        elif key == 'LEFT' and direction != (1, 0):
            direction = (-1, 0)
        elif key == 'RIGHT' and direction != (-1, 0):
            direction = (1, 0)
        elif key == 'R':
            init_game()
            return

def move_snake():
    global snake, game_over, score, pending_growth, speed
    
    if game_over:
        return
    
    # Получаем новую позицию головы
    head_x, head_y = snake[0]
    dx, dy = direction
    new_x = (head_x + dx) % GRID_WIDTH
    new_y = (head_y + dy) % GRID_HEIGHT
    new_head = (new_x, new_y)
    
    # Проверяем столкновение с собой
    if new_head in snake:
        game_over = True
        return
    
    # Добавляем новую голову
    snake.insert(0, new_head)
    
    # Проверяем съедение еды
    if new_head == food:
        score += 10
        pending_growth += 1
        generate_food()
        
        # Увеличиваем скорость каждые 50 очков
        if score % 50 == 0 and speed < 20:
            speed += 1
    elif pending_growth > 0:
        pending_growth -= 1
    else:
        # Удаляем хвост если не растем
        snake.pop()
    
    # Обновляем статистику
    update_stats(score, len(snake), speed)

def draw_game():
    # Очищаем экран
    screen.fill(BACKGROUND)
    
    # Рисуем сетку
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)
    
    # Рисуем змейку
    for i, (x, y) in enumerate(snake):
        color = SNAKE_HEAD if i == 0 else SNAKE_BODY
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (255, 255, 255), rect, 1)
        
        # Глаза для головы
        if i == 0:
            eye_size = GRID_SIZE // 5
            if direction == (1, 0):  # Вправо
                eye1 = (rect.right - eye_size - 2, rect.top + 5)
                eye2 = (rect.right - eye_size - 2, rect.bottom - 5)
            elif direction == (-1, 0):  # Влево
                eye1 = (rect.left + 2, rect.top + 5)
                eye2 = (rect.left + 2, rect.bottom - 5)
            elif direction == (0, 1):  # Вниз
                eye1 = (rect.left + 5, rect.bottom - eye_size - 2)
                eye2 = (rect.right - 5, rect.bottom - eye_size - 2)
            else:  # Вверх
                eye1 = (rect.left + 5, rect.top + 2)
                eye2 = (rect.right - 5, rect.top + 2)
            
            pygame.draw.circle(screen, (0, 0, 0), eye1, eye_size)
            pygame.draw.circle(screen, (0, 0, 0), eye2, eye_size)
    
    # Рисуем еду
    food_rect = pygame.Rect(food[0] * GRID_SIZE, food[1] * GRID_SIZE, 
                           GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, food_rect)
    pygame.draw.rect(screen, (255, 200, 200), food_rect, 2)
    
    # Текст счета
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))
    
    # Если игра окончена
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill(GAME_OVER_BG)
        screen.blit(overlay, (0, 0))
        
        game_over_font = pygame.font.Font(None, 72)
        restart_font = pygame.font.Font(None, 36)
        
        game_over_text = game_over_font.render('GAME OVER', True, (255, 100, 100))
        restart_text = restart_font.render('Press R to restart', True, TEXT_COLOR)
        
        screen.blit(game_over_text, 
                   (WIDTH // 2 - game_over_text.get_width() // 2, 
                    HEIGHT // 2 - 50))
        screen.blit(restart_text, 
                   (WIDTH // 2 - restart_text.get_width() // 2, 
                    HEIGHT // 2 + 20))

def game_loop():
    handle_keys()
    move_snake()
    draw_game()
    
    # Рисуем на HTML canvas
    draw_to_canvas(screen)
    
    # Контроль скорости через sleep (упрощенно)
    import time
    time.sleep(1.0 / speed)

# Инициализируем игру при старте
init_game()

# Для отладки
print("🐍 Snake game initialized!")
print("Use arrow keys to control the snake")
print("Press R to restart")
