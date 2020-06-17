# Jeremiah Baclig - last edit: 4/21/2020 @2AM
# ALL VISUAL/BUTTONS HANDLED MANUALLY FOR PURPOSE
# OF PROJECT

import pygame
import Constants

# draws buttons
def draw_rect(surface):
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button110)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button120)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button130)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button210)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button220)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button230)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button310)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button320)
    pygame.draw.rect(surface, Constants.SKY_BLUE, Constants.button330)
    pygame.draw.rect(surface, Constants.VIOLET_RED, Constants.button_quit)

# defines text and blits to screen
def text():
    from Visualization import surface
    mono_font = pygame.font.SysFont("monospace", 25)
    dimension_font = pygame.font.SysFont("monospace", 14)
    label_per = mono_font.render("|10%|20%|30%|", 1, Constants.WHITE)
    label100 = dimension_font.render("-----100x100-----", 1, Constants.WHITE)
    label200 = dimension_font.render("-----200x200-----", 1, Constants.WHITE)
    label300 = dimension_font.render("-----300x300-----", 1, Constants.WHITE)
    label_quit = mono_font.render("QUIT", 1, Constants.WHITE)
    surface.blit(label_per, (800, 50))
    surface.blit(label100, (825, 160))
    surface.blit(label200, (825, 360))
    surface.blit(label300, (825, 560))
    surface.blit(label_quit, (860, 760))

# handles all button clicks and has inner function to reset constants needed for ARA*
def button_press(event, surface):
    from Visualization import choice

    def clear_constants():
        Constants.SUM = 0
        Constants.PATH = []
        Constants.PATH_DIST = []
        Constants.OBSTACLES = []
        Constants.W0 = 9
        Constants.INFLATION = 10

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if Constants.button110.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button110)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W, Constants.ENDING, Constants.P10, Constants.GRID)
            clear_constants()
        elif Constants.button120.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button120)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W, Constants.ENDING, Constants.P20, Constants.GRID)
            clear_constants()
        elif Constants.button130.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button130)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W, Constants.ENDING, Constants.P30, Constants.GRID)
            clear_constants()
        elif Constants.button210.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button210)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W2, Constants.ENDING2, Constants.P10, Constants.GRID2)
            clear_constants()
        elif Constants.button220.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button220)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W2, Constants.ENDING2, Constants.P20, Constants.GRID2)
            clear_constants()
        elif Constants.button230.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button230)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W2, Constants.ENDING2, Constants.P30, Constants.GRID2)
            clear_constants()
        elif Constants.button310.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button310)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W3, Constants.ENDING3, Constants.P10, Constants.GRID3)
            clear_constants()
        elif Constants.button320.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button320)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W3, Constants.ENDING3, Constants.P20, Constants.GRID3)
            clear_constants()
        elif Constants.button330.collidepoint(mouse_pos):
            pygame.draw.rect(surface, Constants.GREEN, Constants.button330)
            pygame.draw.rect(surface, Constants.BLACK, (0, 0, Constants.WIDTH + 1, Constants.HEIGHT + 1))
            pygame.display.update()
            choice(Constants.W3, Constants.ENDING3, Constants.P30, Constants.GRID3)
            clear_constants()
        elif Constants.button_quit.collidepoint(mouse_pos):
            Constants.END = True
        else:
            draw_rect(surface)
            pygame.display.update()

# handles color change on mouse hover over buttons
def button_hover(surface):
    mouse_pos = pygame.mouse.get_pos()
    if Constants.button110.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button110)
        pygame.display.update()
    elif Constants.button120.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button120)
        pygame.display.update()
    elif Constants.button130.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button130)
        pygame.display.update()
    elif Constants.button210.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button210)
        pygame.display.update()
    elif Constants.button220.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button220)
        pygame.display.update()
    elif Constants.button230.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button230)
        pygame.display.update()
    elif Constants.button310.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button310)
        pygame.display.update()
    elif Constants.button320.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button320)
        pygame.display.update()
    elif Constants.button330.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.POWDER_BLUE, Constants.button330)
        pygame.display.update()
    elif Constants.button_quit.collidepoint(mouse_pos):
        pygame.draw.rect(surface, Constants.PINK, Constants.button_quit)
        pygame.display.update()
    else:
        draw_rect(surface)
        pygame.display.update()
