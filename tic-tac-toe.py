import random
import time

grid_line = """ 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9\n"""

class Tic_Tac_Toe:
    # variable names"
    grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 'X'
    o = 'O'

    # This is how a grid is supposed to look:
    #   1 | 2 | 3 
    #  ---+---+---
    #   4 | 5 | 6 
    #  ---+---+---
    #   7 | 8 | 9

    # 1 ----> (0, 0)
    # 2 ----> (0, 1)
    # 3 ----> (0, 2)
    # 4 ----> (1, 0)
    # 5 ----> (1, 1)
    # 6 ----> (1, 2)
    # 7 ----> (2, 0)
    # 8 ----> (2, 1)
    # 9 ----> (2, 2)

    # defined functions
    def Print_Grid(self):
        for i in range(3):
            print(*self.grid[i])
    
    def Winner_Of_The_Game(self, i):
        for row_col in range(3):
            col1 = self.grid[row_col][0]
            col2 = self.grid[row_col][1]
            col3 = self.grid[row_col][2]

            if col1 == col2 and col1 == col3:
                if col1 == self.x:
                    return self.x
                elif col1 == self.o:
                    return self.o

            row1 = self.grid[0][row_col]
            row2 = self.grid[1][row_col]
            row3 = self.grid[2][row_col]

            if row1 == row2 and row1 == row3:
                if row1 == self.x:
                    return self.x
                elif row1 == self.o:
                    return self.o
        
        diag1 = self.grid[0][0]
        diag2 = self.grid[1][1]
        diag3 = self.grid[2][2]
        diag4 = self.grid[2][0]
        diag5 = self.grid[0][2]

        if diag1 == diag2 and diag2 == diag3:
            if diag1 == self.x:
                return self.x
            elif diag1 == self.o:
                return self.o
        elif diag5 == diag2 and diag5 == diag4:
            if diag4 == self.x:
                return self.x
            elif diag4 == self.o:
                return self.o
            
        if i <= 2:
            return "None"

    def SetUser(self, user_marker):
        self.user_marker = user_marker

    def SetComputer(self, computer_marker):
        self.computer_marker = computer_marker

    def GetUser(self):
        return self.user_marker
    
    def GetComputer(self):
        return self.computer_marker
    
    def Conversion(self, spot):
        switcher = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switcher.get(spot)
    
    def Computer_Input(self):
        return random.randint(self.spots[0], self.spots[len(self.spots) - 1])


game = Tic_Tac_Toe()

print("Hello to the Tic_Tac_Toe Game\n")

while(True):
    user = input("Please select \'X' or \'O': ")

    if (user.upper() == 'X' or user.upper() == 'O'):
        if user.upper() == 'X':
            print(f"You -----> {user.upper()}.")
            game.SetUser(user.upper())
            print("Computer -----> O.\n")
            game.SetComputer('O')
        elif user.upper() == 'O':
            print(f"You -----> {user.upper()}.")
            game.SetUser(user.upper())
            print("Computer -----> X.\n")
            game.SetComputer('X')
        
        break
    else:
        print("Invalid Input. Please try again!!!\n")

print("Here's how the grid is going to look:")

game.Print_Grid()

print('\n')
print("To place your marker on the grid, you need to select the following numbers:")

print(grid_line)

# Note that the user will always start

i = 9

while i != 0:
    user = int(input("Enter your spot number: "))
    computer = game.Computer_Input()

    while not(user >= game.spots[0]) or not(user <= game.spots[len(game.spots) - 1]) or not(user in game.spots):
        print("Invalid Input. Please try again.\n")
        user = int(input("Enter your spot number: "))

    game.spots.remove(user)
    x_user, y_user = game.Conversion(user)
    game.grid[x_user][y_user] = game.GetUser()
    i -= 1

    winner = game.Winner_Of_The_Game(i)

    if i <= 5:
        game.Print_Grid()
        print('\n')
        if winner == 'X':
            if game.GetUser() == winner:
                print("You are the winner!!!!\n")
                break
            elif game.GetComputer() == winner:
                print("The computer is the winner!!!\n")
                break
        elif winner == 'O':
            if game.GetUser() == winner:
                print("You are the winner!!!!\n")
                break
            elif game.GetComputer() == winner:
                print("The computer is the winner!!!\n")
                break
        else:
            if i <= 1 and winner == "None":
                print("It's a draw.\n")
                break

    while not(computer in game.spots) and not(i <= 1):
        computer = game.Computer_Input()
    
    game.spots.remove(computer)
    x_computer, y_computer = game.Conversion(computer)
    game.grid[x_computer][y_computer] = game.GetComputer()
    i -= 1

    print(game.spots)
    print('\n')
    game.Print_Grid()
    print('\n')


print("The End!!!!")