## Zack's rule based model as a .py file so i can import it into the Rule based cnn train file


import numpy as np
import random
import gymnasium as gym
import tetris_gymnasium
from tetris_gymnasium.envs.tetris import ActionsMapping
def printarray(array):
    for row in array:
        print(row)

board1 = [[0, 0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]


# Finds the column heights for attached pieces
def find_column_heights(board):
    column_heights = [0] * 10
    for c in range(10):
        maxHeight = 0
        r = 19
        while r >= 0:
            if board[r][c] != 0 and is_attached(board, c, r):
                maxHeight = 20 - r
            r -= 1
        column_heights[c] = maxHeight
    return column_heights


def is_valid(board, xindex, yindex):
    # Checking out of bounds
    if (yindex >= 20 or yindex < 0 or xindex < 0 or xindex >= 10):
        return False
    # Check if space is not a piece
    elif (board[yindex][xindex] == 0):
        return False
    else:
        return True


# Tested and Approved
# Checks if the piece which contains the position xindex yindex is connected
def is_attached(board, xindex, yindex):
    if (not is_valid(board, xindex, yindex)):
        return False
    queue = [(xindex, yindex)]
    visited = []
    while (len(queue) > 0):
        current_index = queue.pop()
        # print(current_index)
        visited.append(current_index)
        x = current_index[0]
        y = current_index[1]
        if y == 19:
            return True
        if (is_valid(board, x, y - 1) and not ((x, y - 1) in visited)):
            queue.append((x, y - 1))
        if (is_valid(board, x + 1, y) and not ((x + 1, y) in visited)):
            queue.append((x + 1, y))
        if (is_valid(board, x - 1, y) and not ((x - 1, y) in visited)):
            queue.append((x - 1, y))
        if (is_valid(board, x, y + 1) and not ((x, y + 1) in visited)):
            queue.append((x, y + 1))

    return False


# Used to find the coordinates of the active piece
def get_visited(board, xindex, yindex):
    # print(board[yindex][xindex])
    # printarray(board)
    # print(board[yindex])
    if (not is_valid(board, xindex, yindex)):
        # Stands for No Piece Found
        return "NPF"
    queue = [(xindex, yindex)]
    visited = []
    while (len(queue) > 0):
        current_index = queue.pop()
        # print(current_index)
        visited.append(current_index)
        x = current_index[0]
        y = current_index[1]
        if y == 19:
            return visited
        if (is_valid(board, x, y - 1) and not ((x, y - 1) in visited)):
            queue.append((x, y - 1))
        if (is_valid(board, x + 1, y) and not ((x + 1, y) in visited)):
            queue.append((x + 1, y))
        if (is_valid(board, x - 1, y) and not ((x - 1, y) in visited)):
            queue.append((x - 1, y))
        if (is_valid(board, x, y + 1) and not ((x, y + 1) in visited)):
            queue.append((x, y + 1))

    return visited

def is_unattached(board, x_index, y_index):
    if(board[y_index][x_index] == 0):
        #print(f"There is no piece at {x_index, y_index}")
        return False
    elif(not is_attached(board, x_index, y_index)):
        return True
    return False

def find_active_piece(board):
    piece = 0
    xindex = 0
    yindex = 0
    #Row by row scan starting at the top to find the first piece which is unattached
    while(not is_unattached(board, xindex, yindex)):
        if(xindex == 9):
            xindex = 0
            yindex += 1
        else:
            xindex += 1
        if(yindex >= 20):
            #We do this so the is_unattached method doesn't have to deal with out of bounds
            break
    if(yindex < 20):
        piece = board[yindex][xindex]
    if(piece == 0):
        pass
        #print("No active piece found")
    piece_coordinates = get_visited(board, xindex, yindex)
    return piece_coordinates

def find_piece_width(board):
    piece_coordinates = find_active_piece(board)
    x_coordinates = []
    for coordinate in piece_coordinates:
        x_coordinates.append(coordinate[0])
    if(x_coordinates == ["N", "P", "F"]):
        return "No Piece Found"
    #print(x_coordinates)
    #print(x_coordinates == ["N", "P", "F"])
    range = max(x_coordinates) - min(x_coordinates) + 1
    return range

find_piece_width(board1)

def find_leftmost_index(board):
    piece_coordinates = find_active_piece(board)
    x_coordinates = []
    for coordinate in piece_coordinates:
        x_coordinates.append(coordinate[0])
    return min(x_coordinates)

#Finds the location where the robot should aim
def find_aim(column_heights, piece_width):
    if(piece_width == 1):
        aim = np.argmin(column_heights)
    elif(piece_width == 2):
        lowest_2by = []
        #Find the maxes of the current spot and the spot next to it to find the lowest point to fit a 2 wide piece
        for i in range(len(column_heights)-1):
            lowest_2by.append(max(column_heights[i],column_heights[i+1]))
        aim = np.argmin(lowest_2by)
    else:
        print("Piece width exceeded 2, should have been rotated")
    return aim

# --- Initialize the Tetris Environment ---
env = gym.make("tetris_gymnasium/Tetris", render_mode="ansi")

# Get the available actions from ActionsMapping
actions = ActionsMapping()

#Convert string board which is returned by env.render() to an array
def convert_strBoard_to_2dArray(board):
    array = []
    row = []
    for char in board:
        if char != "\n":
            if char == '.':
                row.append(0)
            else:
                row.append(int(char))
        else:
            array.append(row)
            row = []
    array.append(row)
    #printarray(array)
    return array


# --- Function to Extract Board Features ---
def get_board_features(board):
    """
    Extracts meaningful features from the Tetris board.
    """
    column_heights = [0] * 10
    for c in range(10):
        maxHeight = 0
        r = 19
        while r >= 0:
            if board[r][c] != 0:
                maxHeight = 20 - r
            r -= 1
        column_heights[c] = maxHeight
    # print(column_heights)
    # printarray(board)
    max_height = max(column_heights)
    bumpiness = sum(abs(column_heights[i] - column_heights[i + 1]) for i in range(9))
    holes = sum(1 for c in range(10) for r in range(column_heights[c]) if board[r][c] == 0)
    return np.array([max_height, holes, bumpiness])


def play_tetris():
    """
    Plays a single game of Tetris using a genome's weights.
    """
    total_lines_cleared = 0
    total_reward = 0
    state = env.reset()
    done = False

    move_list = []

    while not done:
        board = env.render()  # Get board as image

        #print(type(board))
        board = convert_strBoard_to_2dArray(board)
        column_heights = find_column_heights(board)
        #print(f"column heights: {column_heights}")
        piece_width = find_piece_width(board)
        if(piece_width == "No Piece Found"):
            #Hard drop if the active piece doesn't have anywhere to go
            action = 5
        #Rotate the piece if it is wide
        elif(piece_width > 2):
            action = 3 #Rotate clockwise
        else:
            aim = find_aim(column_heights, piece_width)
            left_index = find_leftmost_index(board)
            if(left_index > aim):
                #Move left
                action = 0
            elif(left_index < aim):
                #Move right
                action = 1
            else:
                #We have found the columns we want the piece to go
                #Hard drop
                action = 5
        #print(action)
        #print(f"action: {action}")
        # Ensure the action is valid
        #action = actions.get(action)  # Map to an action from ActionsMapping
        step_result = env.step(action)  # Store step results in a variable
       # Handle both 4-value and 5-value return cases
        if len(step_result) == 4:
            next_state, reward, done, info = step_result  # Old format
        else:
            next_state, reward, done, truncated, info = step_result  # New format
            done = done or truncated  # Ensure 'done' includes truncation
        #print(truncated)
        total_reward += reward
        #print(info['lines_cleared'])
        #if(info['lines_cleared'] > 0):
            #printarray(board)
            #print(next_state)
        piece_coordinates = find_active_piece(board)
        if not done:
            total_lines_cleared += info['lines_cleared']  # Track lines cleared
        else:
            total_lines_cleared = 0
        move = {"board": board, "piece": piece_coordinates, "action": action, "reward": reward}
        move_list.append(move)

    #print(total_lines_cleared)
    return {"Lines Cleared" : total_lines_cleared, "Reward": total_reward, "Move List":move_list}

def train_model(episodes):
    history = []
    i = 0
    while(i < episodes):
        tetris = play_tetris()
        reward = tetris["Reward"]
        lines_cleared = tetris["Lines Cleared"]
        history.append(tetris)
        print(f"Episode {i}: Reward: {reward}, Lines Cleared: {lines_cleared}")
        i += 1
    return history

history = train_model(100)
