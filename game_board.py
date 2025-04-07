# Comp 141 009
# mine_sweeper - Final Project 
#
# Collaborators: 
# Benjamin Winokur(009)
# Luke Nowolis(009)
# Kaelen Bobber (009)
# Keegan Gallagher (009)
#we have a seperate file that has a random list of bombs and numbers that is going to be attatched to this one to use in the boxes on the gameboard
#we plan to have a list generated with all the bomb locations and then a second list which is whats been revealed and where the user wants flags

import random          
board_size=9#this controls board size we can change it to  whateer we want  
game=0#game is just a varible that will keep our while loop running, once we add one to game-when they hit a bomb, the while loop will stop going 
numbombs=5

num=[] #just a place holder list before we make the real one 
list_one=[] #This is the list that shows us where the bombs are and has the numbers telling us how many bombs there are in adjacent squares
user_list = ['x'] * (board_size ** 2) #this is the list the user will see, thats why I added all the x's, they should have all the tiles coverd up when they start 
zero_list=[]

def find_zeros():
    global zero_list
    zero_list=[i for i, x in enumerate(list_one) if x == 0]
    

def bombs(board_size): #all this does is randomly assign bombs to the place holder list 
    global num
    for i in range(1,board_size**2+1):
        num.append(0)
    bcheck=0
    while bcheck<numbombs:
        x=random.randint(0,(board_size**2)-1)
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

def board_one(board_size): #This is just to show how the list looks in a grid,#this is just for testing to make sure everything is running propperly. We will take it out for the real game
    for i in range(1,(board_size**2)+1):
        if i%board_size!=0:
            print(list_one[i-1],' ',end='')
        else:
            print(list_one[i-1])
        
def is_row(x):#checks if the row input is valid 
    if x in ('1','2','3','4','5','6','7','8','9'):
        return True
    else:
        return False
def is_coloum(x):#checks if the coloum input is valid 
    if x.upper() in ('A','B','C','D','E','F','G','H','I'):#This will have to depend of board_size so we should figure out how big 
        return True
    else:
        return False
def is_action(x):#checks if the action input is valid 
    if x.upper() in ("F","O"):#if they put an f here we can add a flag to this spot on the board, for now if they put an O we can take it as a click on that spot 
        return True
    else:
        return False

def user():#prompts user for what position they want to use next, returns the inndex value of that spot on the board
    global game, numbombs
    n=0
    while n==0:
        row=input("number: ")
        if is_row(row):
            row=int(row)
            coloum=input('letter: ')
            if is_coloum(coloum):
                action=input('action: ')
                if is_action(action):
                    n+=1
                else:
                    print("Bad input")
            else:
                print("Bad input")
        else:
            print("Bad input")
    letters=['A','B','C','D','E','F','G','H','I']
    game=0
    col=letters.index(coloum.upper())
    index=(((row-1)*board_size)+col)
    if action.upper()=='F':#this part here is the flag function of the game 
        if numbombs !=0:
            if user_list[index]=='x':
                user_list[index]='F'
                numbombs-=1
            elif user_list[index]=='F':
                user_list[index]='x'
                numbombs +=1
        else:
            print("Out of flags")
        
    if action.upper()=='O':#this either replaces the value in the user list with the same one from the offical list telling the user how many bombs in area or if the user chooses a space with a bomb it will end the game 
        if list_one[index]=='B':
            print("GAME OVER")
            print("you hit a bomb")
            game+=1
        else:
            area(index,board_size)
            user_list[index]=list_one[index]

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
        
def board_two(board_size): #This is what the user will see and is what needs to be changed when we make our actual board.
    print("   A  B  C  D  E  F  G  H  I")
    print("   |  |  |  |  |  |  |  |  |")
    for i in range(1,board_size+1):
        print(i,'-',end='')
        for a in range(board_size):
            if a==board_size-1:
                print(user_list[(board_size*(i-1))+a],' ')
            else:
                print(user_list[(board_size*(i-1))+a],' ',end='')

def minesweeper_text():
    start_game = ""
    while start_game == "":
        print("  __  __ _")
        print(" |  \/  (_)")
        print(" | \  / |_ _ __   ___  _____      _____  ___ _ __   ___ _ __")
        print(" | |\/| | | '_ \ / _ \/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|")
        print(" | |  | | | | | |  __/\__  \ V  V /  __/  __/ |_) |  __/ |   ")
        print(" |_|  |_|_|_| |_|\___||___/ \_/\_/ \___|\___| .__/ \___|_|   ")
        print("                                            | |              ")
        print("                                            |_|              ")
        print()
        start_game = input("Press The Enter Key to Start: ")
    return


def main():
    global game
    numbers(board_size)
    minesweeper_text()
    print("Rules-")
    print("input a number and a letter to select your tile")
    print("input an O for action if you think it's not a bomb or an F if you hink it is")
    while game==0:
        board_two(board_size)
        print('you have',numbombs,'flags left')
        user()
        flags_check=[i for i, x in enumerate(user_list) if x == 'F']
        bombs_check=[i for i, x in enumerate(list_one) if x == 'B']
        if flags_check==bombs_check:
            game+=1
            print("YOU WON!")
main()
