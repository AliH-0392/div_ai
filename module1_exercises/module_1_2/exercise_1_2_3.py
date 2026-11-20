tic_tac_toe = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', ' ']
    ]

print(f"the element at the center: {tic_tac_toe[1][1]}")
print("\n")
tic_tac_toe[2][2] = "O"
print(f"The new board: \n{tic_tac_toe}")