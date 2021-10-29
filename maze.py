import random

floor = 'f'
wall = 'w'
player = 'p'
enemy = 'e'
undefined = 'u'

height = 10
width = 19


def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(undefined)
        maze.append(line)
    return maze


def message_maze(maze):

    message = ''

    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == undefined:
                message += '⬜'
            elif maze[i][j] == floor:
                message += '⬛'
            elif maze[i][j] == player:
                message += '😃'
            elif maze[i][j] == enemy:
                message += '👾'
            else:
                message += '🟫'
        message += '\n'

    return message


def debug_print_maze(maze):

    message = ''

    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == undefined:
                message += undefined
            elif maze[i][j] == floor:
                message += floor
            elif maze[i][j] == player:
                message += player
            elif maze[i][j] == enemy:
                message += enemy
            else:
                message += wall
        message += '\n'

    return message


def surroundingCells(rand_wall, maze):
    s_cells = 0
    if (maze[rand_wall[0] - 1][rand_wall[1]] == floor):
        s_cells += 1
    if (maze[rand_wall[0] + 1][rand_wall[1]] == floor):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] - 1] == floor):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] + 1] == floor):
        s_cells += 1
    return s_cells


def generate_maze():
    # Randomize starting point and set it a cell
    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)

    if starting_height == 0:
        starting_height += 1
    if starting_height == height - 1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == width - 1:
        starting_width -= 1

    maze = init_maze(width, height)

    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = floor
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1] - 1] == undefined
                    and maze[rand_wall[0]][rand_wall[1] + 1] == floor):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall, maze)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = floor

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != floor):
                            maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Bottom cell
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != floor):
                            maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != floor):
                            maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0] - 1][rand_wall[1]] == undefined
                    and maze[rand_wall[0] + 1][rand_wall[1]] == floor):

                s_cells = surroundingCells(rand_wall, maze)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = floor

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != floor):
                            maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != floor):
                            maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Rightmost cell
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != floor):
                            maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height - 1):
            if (maze[rand_wall[0] + 1][rand_wall[1]] == undefined
                    and maze[rand_wall[0] - 1][rand_wall[1]] == floor):

                s_cells = surroundingCells(rand_wall, maze)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = floor

                    # Mark the new walls
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != floor):
                            maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != floor):
                            maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != floor):
                            maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the right wall
        if (rand_wall[1] != width - 1):
            if (maze[rand_wall[0]][rand_wall[1] + 1] == undefined
                    and maze[rand_wall[0]][rand_wall[1] - 1] == floor):

                s_cells = surroundingCells(rand_wall, maze)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = floor

                    # Mark the new walls
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != floor):
                            maze[rand_wall[0]][rand_wall[1] + 1] = wall
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != floor):
                            maze[rand_wall[0] + 1][rand_wall[1]] = wall
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != floor):
                            maze[rand_wall[0] - 1][rand_wall[1]] = wall
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == undefined):
                maze[i][j] = wall

    # Set entrance and exit
    for i in range(0, width):
        if (maze[1][i] == floor):
            maze[0][i] = floor
            break

    for i in range(width - 1, 0, -1):
        if (maze[height - 2][i] == floor):
            maze[height - 1][i] = floor
            break
  
    return maze