# 1
def spin_words(sentence):
    return " ".join(word[::-1] if len(word)>=5 else word  for word in sentence.split())

# 2
def find_outlier(integers):
    odd = [i for i in integers if i%2 !=0]
    even = [i for i in integers if i%2 ==0]
    return odd[0] if len(odd)< len(even) else even[0]

# 3
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

# 4
def validate_sudoku(board):
    nums = set(range(1,10))
    for i in board:
        if set(i) != nums:
            return False
    for j in zip(* board):
        if j != nums:
            return False
    for i in range(0,7,3):
        for j in range(0,7,3):
            if nums != {board[x][y] for x in range(i,i+3) for y in range(j,j+3)}:
                return False
    return True

# 5
def triangle(row):
    reduce = [3**i+1 for i in range(10)][::-1]
    
    color = {'GG':'G', 'BB':'B', 'RR':'R', 'BR':'G', 
            'BG':'R', 'GB':'R', 'GR':'B', 'RG':'B', 'RB':'G'}
    
    for length in reduce:
        while len(row)>=length:
            row = [color[row[i]+row[length+i-1]] for i in range(len(low)-length+1)]
    return row[0]
    