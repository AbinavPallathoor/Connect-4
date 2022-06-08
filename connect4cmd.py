grid = [[0,0,0,0,0,0,0,], [0,0,0,0,0,0,0,], [0,0,0,0,0,0,0,], [0,0,0,0,0,0,0,], [0,0,0,0,0,0,0,], [0,0,0,0,0,0,0,]]

render_grid_list = grid
def render_grid():
    grid_string = ''
    for row in render_grid_list:
        for item in row:
            if item == 0:
                grid_string += '⚪'
            elif item == 1:
                grid_string += '🔴'
            elif item == 2:
                grid_string += '🔵'
        grid_string += '\n'
    grid_string += '1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ \n'
    return grid_string

def add_coin(column, player):
    try: int(column)
    except: return True
    if column > 6:
        return True
    elif grid[5][column] == 0:
        grid[5][column] = player
        return False
    elif grid[4][column] == 0:
        grid[4][column] = player
        return False
    elif grid[3][column] == 0:
        grid[3][column] = player
        return False
    elif grid[2][column] == 0:
        grid[2][column] = player
        return False
    elif grid[1][column] == 0:
        grid[1][column] = player
        return False
    elif grid[0][column] == 0:
        grid[0][column] = player
        return False
    else:
        return True

def check_winner():
    # Check Horizontal
    for row in grid:
        check = str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]) + str(row[4]) + str(row[5]) + str(row[6])
        if '1111' in check:
            print('👑 PLAYER 1 WINS 👑')
            return True
        if '2222' in check:
            print('👑 PLAYER 2 WINS 👑')
            return True
    
    # Check Vertical
    for i in range(6):
        check = ''
        for row in grid:
            check += str(row[i])
        if '1111' in check:
            print('👑 PLAYER 1 WINS 👑')
            return True
        if '2222' in check:
            print('👑 PLAYER 2 WINS 👑')
            return True
    
    # Check Diagonal
    flip_grid = grid[::-1]

    for ri in range(3):
        check = ''
        check2 = ''
        check3 = ''
        check4 = ''
        for i, row in enumerate(grid):
            if i + ri <= 5:
                check4 += str(flip_grid[i][i + ri + 1])
                check3 += str(flip_grid[i + ri][i])
                check2 += str(grid[i][i + ri + 1])
                check += str(grid[i + ri][i])
        if '1111' in check or '1111' in check2 or '1111' in check3 or '1111' in check4:
            print('👑 PLAYER 1 WINS 👑')
            return True
        if '2222' in check or '2222' in check2 or '2222' in check3 or '2222' in check4:
            print('👑 PLAYER 2 WINS 👑')
            return True


i = 1
while True:
    print(render_grid())
    if check_winner():
        break
    playAgain = True
    if i % 2 == 0:
        while playAgain:
            column = input('🔵 Player 2 place your coin in column: ')
            try: 
                column = int(column) - 1
                playAgain = add_coin(column, 2)
            except: pass
    else:
        while playAgain:
            column = input('🔴 Player 1 place your coin in column: ')
            try:
                column = int(column) - 1
                playAgain = add_coin(column, 1)
            except: pass
    i += 1