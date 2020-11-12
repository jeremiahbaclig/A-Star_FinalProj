# Jeremiah Baclig - last edit: 4/23/2020 @3PM

import pygame, sys, random, math, time
import constants
from buttons import draw_rect
from buttons import button_hover
from buttons import button_press
from buttons import text


# Randomly generates obstacles - draws them red and returns the coordinates of them
def random_fill(x, y, w, p):
    obstacle = (x, y)

    rand = random.randint(0, 50)
    if rand < p:
        pygame.draw.rect(surface, constants.RED, (x, y, w, w))
        return obstacle


# draws in the correctly sized grid and calls random_fill() for obstacles
def draw(w, p, grid):
    obst_list = []
    x, y = 0, 0

    for row in grid:
        for col in row:
            pygame.draw.rect(surface, constants.BLUE, (x, y, w, w), 1)

            if x == 0 and y == 0:
                pygame.draw.rect(surface, constants.GREEN, (x, y, w, w))
                pass
            elif x == 792 and y == 792 or x == 796 and y == 796 or x == constants.END_3X and y == constants.END_3Y:
                continue
            else:
                val = random_fill(x, y, w, p)
                if val is not None:
                    obst_list.append(val)

            pygame.display.update()
            x = x + w
        y = y + w
        x = 0

    return obst_list


# straight line distance used for g
def distance(nx, ny, gx, gy):
    g = math.sqrt((abs(gx - nx) ** 2) + (abs(gy - ny) ** 2))
    return g  # + h


# manhattan distance used for h
def manhattan(nx, ny, gx, gy):
    h = math.sqrt(abs(nx - gx) + abs(ny - gy))
    return h


# Generates all neighbors of the current node and removes based on if it is an obstacle, or if that node has been
# traveled to before. Applies heuristic to neighbors and travels based on minimum f score. Recursively calls itself
# and stores the path that it took for the repairing method.
def astar(x, y, blocked, end, w):
    current = (x, y)
    all_neighbors = [(x + w, y), (x, y + w), (x + w, y + w),
                     (x - w, y - w), (x - w, y), (x - w, y + w),
                     (x, y - w), (x + w, y - w)]

    for i in blocked:
        if i in all_neighbors:
            all_neighbors.remove(i)

    for i in constants.PATH:
        if i in all_neighbors:
            all_neighbors.remove(i)

    neighbor_list1 = heuristic(all_neighbors, end)

    try:
        shortest = min(neighbor_list1, key=neighbor_list1.get)
        constants.SUM += neighbor_list1.get(shortest)
        for val, key in neighbor_list1.items():
            if 0 <= val[0] < 800 and 0 <= val[1] < 800:
                if val == shortest:
                    current = val
                    pygame.draw.rect(surface, constants.GREEN, (*current, w, w))
                    pygame.time.wait(1)
                    pygame.display.update()

                    constants.PATH_DIST.append(key)
                    try:
                        current_index = constants.PATH_DIST.index(key)
                        if constants.PATH_DIST[current_index] > constants.PATH_DIST[current_index - 3]:
                            if (constants.PATH_DIST[current_index] - constants.PATH_DIST[current_index - 3]) < 100:
                                blocked.append(current)
                    except IndexError:
                        continue

    except ValueError:
        pass

    constants.PATH.append(current)

    try:
        if current != end:
            astar(*current, blocked, end, w)
    except RecursionError:
        current_id = constants.PATH.index(current)
        if current != constants.START and constants.PATH[current_id - 1] != constants.START:
            blocked.append(current)
            blocked.append(constants.PATH[current_id - 1])
        # print("(R)")

    return constants.SUM, constants.PATH


# Takes in neighbor list and using a dictionary, stores the coordinates and calculated f score. Returns dictionary.
def heuristic(neighbors, end):
    neighbor_list = {}
    counter = 0

    if counter != len(neighbors):
        for i in neighbors:
            dist = distance(*i, *end) + (constants.INFLATION * manhattan(*i, *end))  # CONSTANT ENDING
            neighbor_list[i] = dist
            counter += 1

    return neighbor_list


# Method to visually clear the path that was taken - clears up for next iteration.
def clear(path, w):
    for i in path:
        pygame.draw.rect(surface, constants.SEA_GREEN, (*i, w, w))

# iterates based on a decrementing W0, decremented inflation e is applied to the heuristic
def repairing(path_sum, blocked, path, end, w):
    start_time = time.time()
    while constants.W0 > 0:
        clear(path, w)
        pygame.draw.rect(surface, constants.GREEN, (*end, w, w))
        pygame.display.update()

        constants.PATH.clear()

        sum_next = astar(*constants.START, blocked, end, w)
        half_val = math.floor(sum_next[0] / 2)

        if sum_next[0] < path_sum:
            clear(path, w)
            pygame.display.update()
        elif half_val == math.floor(path_sum):
            break

        if constants.INFLATION >= 1:
            constants.INFLATION -= 1

        constants.W0 -= constants.W1
    print("RUN TIME: %s seconds" % (time.time() - start_time))

# called based on button press
def choice(w, end, p, grid):
    start_time = time.time()

    constants.OBSTACLES = draw(w, p, grid)
    print("GRID GENERATION: %s seconds" % (time.time() - start_time))

    traveled = astar(*constants.START, constants.OBSTACLES, end, w)
    repairing(traveled[0], constants.OBSTACLES, traveled[1], end, w)
    pygame.display.update()


# main function
def main():
    surface.fill(constants.BLACK)
    text()

    while constants.END is False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_press(event, surface)
            if event.type == pygame.QUIT:
                sys.exit()
            draw_rect(surface)
            button_hover(surface)


pygame.init()
surface = pygame.display.set_mode((constants.WIDTH + 200, constants.HEIGHT))
main()
