# Jeremiah Baclig - last edit: 4/21/2020 @2AM
# ALL VISUAL/BUTTONS HANDLED MANUALLY FOR PURPOSE
# OF PROJECT

import pygame
import constants

# draws buttons
def draw_rect(surface):
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button110)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button120)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button130)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button210)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button220)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button230)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button310)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button320)
    pygame.draw.rect(surface, constants.SKY_BLUE, constants.button330)
    pygame.draw.rect(surface, constants.VIOLET_RED, constants.button_quit)

# defines text and blits to screen
def text():
    from visualization import surface
    mono_font = pygame.font.SysFont("monospace", 25)
    dimension_font = pygame.font.SysFont("monospace", 14)
    label_per = mono_font.render("|10%|20%|30%|", 1, constants.WHITE)
    label100 = dimension_font.render("-----100x100-----", 1, constants.WHITE)
    label200 = dimension_font.render("-----200x200-----", 1, constants.WHITE)
    label300 = dimension_font.render("-----300x300-----", 1, constants.WHITE)
    label_quit = mono_font.render("QUIT", 1, constants.WHITE)
    surface.blit(label_per, (800, 50))
    surface.blit(label100, (825, 160))
    surface.blit(label200, (825, 360))
    surface.blit(label300, (825, 560))
    surface.blit(label_quit, (860, 760))

# handles all button clicks and has inner function to reset constants needed for ARA*
def button_press(event, surface):
    from visualization import choice

    def clear_constants():
        constants.SUM = 0
        constants.PATH = []
        constants.PATH_DIST = []
        constants.OBSTACLES = []
        constants.W0 = 9
        constants.INFLATION = 10

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if constants.button110.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button110)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W, constants.ENDING, constants.P10, constants.GRID)
            clear_constants()
        elif constants.button120.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button120)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W, constants.ENDING, constants.P20, constants.GRID)
            clear_constants()
        elif constants.button130.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button130)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W, constants.ENDING, constants.P30, constants.GRID)
            clear_constants()
        elif constants.button210.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button210)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W2, constants.ENDING2, constants.P10, constants.GRID2)
            clear_constants()
        elif constants.button220.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button220)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W2, constants.ENDING2, constants.P20, constants.GRID2)
            clear_constants()
        elif constants.button230.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button230)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W2, constants.ENDING2, constants.P30, constants.GRID2)
            clear_constants()
        elif constants.button310.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button310)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W3, constants.ENDING3, constants.P10, constants.GRID3)
            clear_constants()
        elif constants.button320.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button320)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W3, constants.ENDING3, constants.P20, constants.GRID3)
            clear_constants()
        elif constants.button330.collidepoint(mouse_pos):
            pygame.draw.rect(surface, constants.GREEN, constants.button330)
            pygame.draw.rect(surface, constants.BLACK, (0, 0, constants.WIDTH + 1, constants.HEIGHT + 1))
            pygame.display.update()
            choice(constants.W3, constants.ENDING3, constants.P30, constants.GRID3)
            clear_constants()
        elif constants.button_quit.collidepoint(mouse_pos):
            constants.END = True
        else:
            draw_rect(surface)
            pygame.display.update()

# handles color change on mouse hover over buttons
def button_hover(surface):
    mouse_pos = pygame.mouse.get_pos()
    if constants.button110.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button110)
        pygame.display.update()
    elif constants.button120.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button120)
        pygame.display.update()
    elif constants.button130.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button130)
        pygame.display.update()
    elif constants.button210.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button210)
        pygame.display.update()
    elif constants.button220.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button220)
        pygame.display.update()
    elif constants.button230.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button230)
        pygame.display.update()
    elif constants.button310.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button310)
        pygame.display.update()
    elif constants.button320.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button320)
        pygame.display.update()
    elif constants.button330.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.POWDER_BLUE, constants.button330)
        pygame.display.update()
    elif constants.button_quit.collidepoint(mouse_pos):
        pygame.draw.rect(surface, constants.PINK, constants.button_quit)
        pygame.display.update()
    else:
        draw_rect(surface)
        pygame.display.update()
