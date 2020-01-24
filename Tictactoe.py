import time
playing = True
turn = 'X'
print("Welcome to Leon Orou's TicTacToe game!")

ticked_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}


# for restart of the game: overriting ticked board with unticked board
new_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}


def printed_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])


def player_won():
    print(f'{turn} won! Congratulations!')
    print('Play again? [y] or [n]')
    play_again = input()
    if play_again == 'y':
        global ticked_board
        ticked_board = new_board  # resetting the board
        return ticked_board
    elif play_again == 'n':
        print('Thank you for playing!')
        time.sleep(3)
        exit()


def won():
    # comparing top row
    if ticked_board['top-L'] == 'X' and ticked_board['top-M'] == 'X' and ticked_board['top-R'] == 'X':
        player_won()
    if ticked_board['top-L'] == 'O' and ticked_board['top-M'] == 'O' and ticked_board['top-R'] == 'O':
        player_won()
    # comparing mid row
    if ticked_board['mid-L'] == 'X' and ticked_board['mid-M'] == 'X' and ticked_board['mid-R'] == 'X':
        player_won()
    if ticked_board['mid-R'] == 'O' and ticked_board['mid-M'] == 'O' and ticked_board['mid-R'] == 'O':
        player_won()
    # comparing bot row
    if ticked_board['bot-L'] == 'X' and ticked_board['bot-M'] == 'X' and ticked_board['bot-R'] == 'X':
        player_won()
    if ticked_board['bot-L'] == 'O' and ticked_board['bot-M'] == 'O' and ticked_board['bot-R'] == 'O':
        player_won()
    # comparing left column
    if ticked_board['top-L'] == 'X' and ticked_board['mid-L'] == 'X' and ticked_board['bot-L'] == 'X':
        player_won()
    if ticked_board['top-L'] == 'O' and ticked_board['mid-L'] == 'O' and ticked_board['bot-L'] == 'O':
        player_won()
    # comparing mid column
    if ticked_board['top-M'] == 'X' and ticked_board['mid-M'] == 'X' and ticked_board['bot-M'] == 'X':
        player_won()
    if ticked_board['top-M'] == 'O' and ticked_board['mid-M'] == 'O' and ticked_board['bot-M'] == 'O':
        player_won()
    # comparing right column
    if ticked_board['top-R'] == 'X' and ticked_board['mid-R'] == 'X' and ticked_board['bot-R'] == 'X':
        player_won()
    if ticked_board['top-R'] == 'O' and ticked_board['mid-R'] == 'O' and ticked_board['bot-R'] == 'O':
        player_won()
    # comparing diagonals
    if ticked_board['top-L'] == 'X' and ticked_board['mid-M'] == 'X' and ticked_board['bot-R'] == 'X':
        player_won()
    if ticked_board['top-L'] == 'O' and ticked_board['mid-M'] == 'O' and ticked_board['bot-R'] == 'O':
        player_won()
    if ticked_board['top-R'] == 'X' and ticked_board['mid-M'] == 'X' and ticked_board['bot-L'] == 'X':
        player_won()
    if ticked_board['top-R'] == 'O' and ticked_board['mid-M'] == 'O' and ticked_board['bot-L'] == 'O':
        player_won()


while playing:
    printed_board(ticked_board)
    print(f'Turn for {turn}. Move on which space? top-, mid-, bot-, left(L), middle(M), right(R)?')
    moved = False
    while not moved:  # look if the place of the move is valid or already taken
        move = input()
        if move not in ticked_board.keys():
            print('Please type a valid move')
        if move in ticked_board.keys():
            if ticked_board.get(move) == 'X' or ticked_board.get(move) == 'O':
                print(f'Ops! there is already {ticked_board.get(move)}! Please type another move')
            else:
                break
        time.sleep(1.5)
    ticked_board[move] = turn
    won()
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
