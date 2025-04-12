import random          
board_size=0#this controls board size we can change it to  whateer we want  
numbombs=0 #changing to zero, both board_size and numboimbs will change based on the game mode
num_flags = 0

game=0#game is just a varible that will keep our while loop running, once we add one to game-when they hit a bomb, the while loop will stop going 
num=[] #just a place holder list before we make the real one 
list_one=[] #This is the list that shows us where the bombs are and has the numbers telling us how many bombs there are in adjacent squares
user_list = ['x'] * (board_size ** 2) #this is the list the user will see, thats why I added all the x's, they should have all the tiles coverd up when they start 
zero_list=[]
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
grid_row_nums = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]

def set_difficulty():
    global board_size, numbombs, user_list, letters, grid_row_nums, num_flags
    print("Select Difficulty: Easy, Medium, or Hard")
    while True:
        choice = input("Enter difficulty (easy/medium/hard): ").lower()
        if choice == "easy":
            board_size = 9
            numbombs = 12
            letters = letters[0:9]
            grid_row_nums = grid_row_nums[0:9]
            break
        elif choice == "medium":
            board_size = 14
            numbombs = 32
            letters = letters[0:14]
            grid_row_nums = grid_row_nums[0:14]
            break
        elif choice == "hard":
            board_size = 26
            numbombs = 85
            letters = letters
            grid_row_nums = grid_row_nums
            break
        else:
            print("Invalid choice. Please type easy, medium, or hard.")

    user_list[:] = ['x'] * (board_size ** 2)
    num_flags = numbombs



def find_zeros():
    global zero_list
    zero_list=[i for i, x in enumerate(list_one) if x == 0]

def bombs(board_size): #all this does is randomly assign bombs to the place holder list 
    global num
    for i in range(1, board_size**2+1):
        num.append(0)
    bcheck=0
    while bcheck < numbombs:
        x = random.randint(0,(board_size**2)-1)
        if num[x] != 1:
            num[x]=1
            bcheck+=1
       
def numbers(board_size):# This takes the place holder list and checks it for where the bombs are and then counts those up so that it displays how many bombs are adjacent to each tile. Values are B,1,2,3,4,5,6,7,8,9
    global list_one
    bombs(board_size)
    for i in range(0,(board_size**2)):
        if num[i]==1:
            list_one.append('B')
        else:
            n=check(i,board_size)
            list_one.append(n)
    find_zeros()

def check(i,board_size):
    n = 0 #counter of how many bombs are adjacent 
    side = i //board_size  #rest of this function is just checking each position around the given tile 
    down = i % board_size
    if side > 0 and down > 0 and num[i - board_size - 1] == 1:
        n += 1
       
    if side > 0 and num[i - board_size] == 1:
        n += 1
       
    if side > 0 and down < board_size - 1 and num[i - board_size + 1] == 1:
        n += 1
       
    if down > 0 and num[i - 1] == 1:
        n += 1
       
    if down < board_size - 1 and num[i + 1] == 1:
        n += 1

    if side < board_size - 1 and down > 0 and num[i + board_size - 1] == 1:
        n += 1

    if side < board_size - 1 and num[i + board_size] == 1:
        n += 1

    if side < board_size - 1 and down < board_size - 1 and num[i + board_size + 1] == 1:
        n += 1

    return n

def user():
    global game, numbombs, num_flags

    while True:
        inp = input("Enter number letter action (e.g., 3 C F): ").split()

        if len(inp) != 3:
            print("Wrong input! Format: number letter action")
            continue

        row, col_letter, action = inp

        # Validate row
        if not is_row(row):
            print("Invalid row! Must be 1-",board_size,".", sep="")
            continue
        row = int(row)

        # Validate column
        if not is_coloum(col_letter):
            print("Invalid column! Must be A-",letters[-1],".", sep="")
            continue
        col = letters.index(col_letter.upper())

        # Validate action
        if not is_action(action):
            print("Invalid action! Use 'F' to flag or 'O' to open.")
            continue

        # Index calculation
        index = ((row - 1) * board_size) + col

        # Action handling
        if action.upper() == 'F':
            if user_list[index] == 'x':
                if num_flags > 0:
                    user_list[index] = 'F'
                    num_flags -= 1
                    break
                else:
                    print("No flags remaining!")
            elif user_list[index] == 'F':
                user_list[index] = 'x'
                num_flags += 1
                break
            else:
                print("Can't flag this tile.")
        elif action.upper() == 'O':
            if list_one[index] == 'B':
                print("GAME OVER - You hit a bomb!")
                game += 1
                break
            else:
                area(index, board_size)
                user_list[index] = list_one[index]
                break         
def is_row(x):#checks if the row input is valid 
    if x in grid_row_nums:
        return True
    else:
        return False
def is_coloum(x):#checks if the coloum input is valid 
    if x.upper() in letters:
        return True
    else:
        return False
def is_action(x):#checks if the action input is valid 
    if x.upper() in ("F","O"):#if they put an f here we can add a flag to this spot on the board, for now if they put an O we can take it as a click on that spot 
        return True
    else:
        return False

def area(i,board_size):
    global user_list
    global zero_list
    if i in zero_list:
        zero_list.remove(i)
    side = i //board_size  #rest of this function is just checking each position around the given tile 
    down = i % board_size
    if side > 0 and down > 0 and list_one[i - board_size - 1] != "B":
        if (i - board_size - 1) in zero_list:
            area(i - board_size - 1,board_size)
        user_list[i - board_size - 1]=list_one[i - board_size - 1]
       
    if side > 0 and list_one[i - board_size] != "B":
        if (i - board_size) in zero_list:
            area(i - board_size,board_size)
        user_list[i - board_size]=list_one[i - board_size]
       
    if side > 0 and down < board_size - 1 and list_one[i - board_size + 1] != "B":
        if (i - board_size + 1) in zero_list:
            area(i - board_size+1,board_size)
        user_list[i - board_size + 1]=list_one[i - board_size + 1]
       
    if down > 0 and list_one[i - 1] != "B":
        if (i - 1) in zero_list:
            area(i - 1,board_size)
        user_list[i - 1]=list_one[i - 1]
       
    if down < board_size - 1 and list_one[i + 1] != "B":
        if (i + 1) in zero_list:
            area(i +1,board_size)
        user_list[i + 1]=list_one[i + 1]

    if side < board_size - 1 and down > 0 and list_one[i + board_size - 1] != "B":
        if (i + board_size - 1) in zero_list:
            area(i + board_size-1,board_size)
        user_list[i + board_size - 1]=list_one[i + board_size - 1]

    if side < board_size - 1 and list_one[i + board_size] != "B":
        if (i + board_size) in zero_list:
            area(i + board_size,board_size)
        user_list[i + board_size]=list_one[i + board_size]

    if side < board_size - 1 and down < board_size - 1 and list_one[i + board_size + 1] != "B":
        if (i + board_size + 1) in zero_list:
            area(i + board_size+1,board_size)
        user_list[i + board_size + 1]=list_one[i + board_size + 1]
        
def colorize(value):
    colors = {
    "0": "\033[30m",     # Black
    "1": "\033[94m",     # Blue
    "2": "\033[92m",     # Green
    "3": "\033[93m",     # Yellow
    "4": "\033[95m",     # Magenta
    "5": "\033[96m",     # Cyan
    "6": "\033[91m",     # Red
    "7": "\033[93;1m",   # Bright Yellow
    "8": "\033[94;1m",   # Bright Blue
    "F": "\033[91;1m",   # Bright Red
    "B": "\033[91m",     # Red for bombs if shown (like game over)
    }
    endc = "\033[0m"  # Reset color
    return f"{colors.get(str(value), '')}{value}{endc}" if value != 'x' else value

def board_two(board_size):
    print("  ", end="")
    index = 0
    while index <= (len(letters)-1):
        if index == (len(letters)-1):
            print("  ", letters[index], sep="")
        else:
            print("  ", letters[index], sep="", end="")
        index += 1

    print("  ", end="")
    index = 0
    while index <= (len(letters)-1):
        if index == (len(letters)-1):
            print("  |", sep="")
        else:
            print("  |", sep="", end="")
        index += 1

    for i in range(1, board_size + 1):
        print(f"{i:2}- ", end="")  # Print row number with alignment
        for a in range(board_size):
            tile = user_list[(board_size * (i - 1)) + a]
            display = colorize(str(tile))
            if a == board_size - 1:
                print(display, ' ')
            else:
                print(display, ' ', end='')


def minesweeper_text(): #loads the "game intro" that is the word minesweeper and doesnt start until given input
    while True:
        print("  __  __ _")
        print(" |  \\/  (_)")
        print(" | \\  / |_ _ __   ___  _____      _____  ___ _ __   ___ _ __")
        print(" | |\\/| | | '_ \\ / _ \\/ __\\ \\ /\\ / / _ \\/ _ \\ '_ \\ / _ \\ '__|")
        print(" | |  | | | | | |  __/\\__ \\\\ V  V /  __/  __/ |_) |  __/ |   ")
        print(" |_|  |_|_|_| |_|\\___||___/ \\_/\\_/ \\___|\\___| .__/ \\___|_|   ")
        print("                                            | |              ")
        print("                                            |_|              ")
        print()
        title_input = input("Press enter to play!")
        if title_input == "":
            return

def minesweeper_rules(): #rules for the game
    print("--------------------------------Minesweeper Rules-----------------------------------------------")
    print("there arebombs hidden on the board. You must find and flag them all.")
    print()
    print("Input a number and a letter to select your tile in relation to the coordinate of the tile.")
    print("Next, input an O for action if you think it's not a bomb or an F if you think it is.")
    print()
    print("If you input an o on a bomb you will lose, if there is not a bomb the tile will reveal a number.")
    print("The number corresponds to the amound of bombs in the six tiles adjacent to the number.")
    print("The flag is a way to mark where believed bombs are to solve the puzzle.")
    print("Use all yout flags correctly to win!")
    print("------------------------------------------------------------------------------------------------")
    print()


def main():
    global game
    minesweeper_text()
    minesweeper_rules()
    set_difficulty()
    numbers(board_size)
    print("Controls-")
    print("input a number and a letter to select your tile")
    print("input an O for action if you think it's not a bomb or an F if you hink it is")
    while game==0:
        board_two(board_size)
        print('you have',num_flags,'flags left')
        user()
        flags_check=[i for i, x in enumerate(user_list) if x == 'F']
        bombs_check=[i for i, x in enumerate(list_one) if x == 'B']
        if flags_check==bombs_check:
            game+=1
            print("YOU WON!")


main()
