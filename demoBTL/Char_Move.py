import G_Var
# 4 top of char check box
def check_collision(matrix,a,b,c,d):
    if matrix[a[0]//30][a[1]//30] != 0: return False
    if matrix[b[0]//30][b[1]//30] != 0: return False
    if matrix[c[0]//30][c[1]//30] != 0: return False
    if matrix[d[0]//30][d[1]//30] != 0: return False
    return True

# move char with distance (a, b)
def move(matrix,a,b,x,y):
    # distance move
    a *= G_Var.speed
    b *= G_Var.speed
    # distance from char to the wall
    diff = 5
    height = 20
    width = 10
    top_left = (x+a+diff,y+b+diff)
    top_right = (x+a+diff,y+b+diff+width)
    bottom_left = (x+a+diff+height,y+b+diff)
    bottom_right = (x+a+diff+height,y+b+diff+width)
    if check_collision(matrix,top_left,top_right,bottom_left,bottom_right):
        return x+a, y+b
    else: return x, y