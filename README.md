# mine_sweeper
The classic game of minesweeper where a randomized board is spawned with bombs and blocks with numbers relating to the location of bombs. Each selection of where to click will reveal a number relating to the number of “bombs” touching that space. If a bomb is selected the player loses.
# MINESWEEPER GAME PLAN

# DISPLAY TITLE SCREEN WITH GAME NAME
# SHOW BRIEF INSTRUCTIONS TO PLAYER
# ASK PLAYER TO SELECT DIFFICULTY LEVEL

# SET UP GAME BOARD BASED ON DIFFICULTY
# PLACE BOMBS RANDOMLY ON THE BOARD
# CALCULATE NUMBERS FOR ALL SAFE SPACES
# MARK ALL TILES AS HIDDEN TO START

# MAIN GAME LOOP STARTS HERE
# SHOW CURRENT BOARD STATE WITH HIDDEN/VISIBLE TILES
# DISPLAY REMAINING FLAGS COUNT
# ASK PLAYER FOR THEIR MOVE (ROW, COLUMN, ACTION)

# IF PLAYER CHOOSES TO FLAG A TILE
# TOGGLE FLAG ON THAT POSITION
# UPDATE REMAINING FLAGS COUNT

# IF PLAYER CHOOSES TO REVEAL A TILE
# CHECK IF TILE CONTAINS A BOMB
# IF BOMB - GAME OVER, PLAYER LOSES
# IF NUMBER - SHOW THAT NUMBER
# IF ZERO - REVEAL IT AND ALL CONNECTED ZEROS

# WHEN REVEALING ZERO TILES
# AUTOMATICALLY SHOW ALL ADJACENT ZEROS
# ALSO REVEAL NUMBER TILES BORDERING ZERO AREAS
# THIS CREATES CHAIN REACTION OF REVEALS

# CHECK FOR WIN CONDITION
# IF ALL BOMBS ARE CORRECTLY FLAGGED
# AND NO WRONG FLAGS EXIST - PLAYER WINS
