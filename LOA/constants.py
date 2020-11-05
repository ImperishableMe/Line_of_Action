
ROW, COL = 8, 8
WIDTH , HEIGHT = 600, 600
SQ_SIZE = WIDTH // ROW

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW_BACK = (255, 204, 153)
YELLOW_TOP = (255, 178, 102)
GREEN = (0, 255, 0)

## constants setter
def setRow(row):
    global ROW
    ROW = row

def setCol(col):
    global COL 
    COL = col