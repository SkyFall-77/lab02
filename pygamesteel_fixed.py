import pygame

pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)

# Создаём окно и сохраняем поверхность в переменную screen
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Lab 02 — AppSec")

# Задаём цвет фона
bg_color = (255, 255, 255)

# Создаём текст
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (screen_width // 2, screen_height // 2)

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Полностью заливаем фон белым цветом
    screen.fill(bg_color)

    # Выводим текст
    screen.blit(text, text_rect)

    # Обновляем содержимое окна
    pygame.display.flip()
