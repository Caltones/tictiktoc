
board = []
def input_int_with_range(max_num:int,req:str)->int:
  while True:
    num = input(f'Enter you {req} number(1-3): ')
    if num.isdigit() and int(num) <= max_num and int(num) > 0:
      return int(num)
    print('Invaild number')

def input_user_selection(player: bool)->None:
  string = 'X'
  if not player:
    string = 'O'
  print(f"\nIt's '{string}' turn!")
  while True:
    row = input_int_with_range(3,'row') -1
    col = input_int_with_range(3,'col') -1
    if board[row][col] == ' ':
      break
    print('This location has been captured!')
  board[row][col] = string
  
def display(board):
  res = '\nThe Game Board\n '
  for i in board: 
    res += '------------\n'
    for j in i:
      res += '|'
      if j=='O':
        res += ' O '
        continue
      if j=='X':
        res +=' X '
        continue
      res += '   '
    res += '|'
    res +='\n '
  res += '------------'
  return res

def check_win_by_row(board)->bool:
  for i in board:
    if len(set(i)) == 1 and  ' ' not in i:
      return True
  return False

def check_win_by_col(board)->bool:
  cur_col = 0
  while cur_col <=2:
    temp = []
    for i in range(3):
      temp.append(board[i][cur_col])
    if len(set(temp)) == 1 and  ' ' not in temp:
      return True
    cur_col += 1
  return False

def check_win_by_cross(board)->bool:
  temp = []
  for i in range(3):
    temp.append(board[i][i])
  if len(set(temp)) == 1 and ' ' not in temp:
    return True
  temp.clear()
  for i in range(2,-1,-1):
    temp.append(board[i][i])
  if len(set(temp)) == 1 and  ' ' not in temp:
    return True
  return False

def main():
  player = True 
  turn = 0
  for i in range(3):
    board.append([' ',' ',' '])
  while turn < 9:
    input_user_selection(player)
    print(display(board))
    if check_win_by_row(board) or check_win_by_col(board) or check_win_by_cross(board):
      if player:
        print("'X' player wins!")
        return
      else:
        print("'O' player wins!")
        return
    player = not player
    turn += 1
  print("It's a tie!")
main()
  