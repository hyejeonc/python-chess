row = ['1', '2', '3', '4', '5', '6', '7', '8']
column = ['a', 'b', 'c', 'd', 'e', 'f', 'G', 'H']
test = [ [2, 3, 4, 5, 6, 4, 3, 2],
[1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[-1, -1, -1, -1, -1, -1, -1, -1],
[-2, -3, -4, -5, -6, -4, -3, -2] ]

def showPosition(mm):
    m = mm
    for i in range(8):
        for j in range(8):
            if m[i][j] == 1:
                m[i][j] = '♟'
            elif m[i][j] == -1:
                m[i][j] = '♙'
            elif m[i][j] == 2:
                m[i][j] = '♜'
            elif m[i][j] == -2:
                m[i][j] = '♖'
            elif m[i][j] == 3:
                m[i][j] = '♞'
            elif m[i][j] == -3:
                m[i][j] = '♘' 
            elif m[i][j] == 4:
                m[i][j] = '♝'
            elif m[i][j] == -4:
                m[i][j] = '♗'   
            elif m[i][j] == 5:
                m[i][j] = '♛'
            elif m[i][j] == -5:
                m[i][j] = '♕'  
            elif m[i][j] == 6:
                m[i][j] = '♚'
            elif m[i][j] == -6:
                m[i][j] = '♔'  
            else:
                m[i][j] = ' '
    print("\n ***** Chess board *****\n")
    print("\n   a  b  c  d  e  f  g  h\n")
    for i in range(8):
        print(8 - i, end='  ')
        for j in range(8):
            print(m[i][j], end= '  ')
        print("\n")
    return m

#showPosition(test)
#print(showPosition(test))

def setPosition(s):
    j = ord(s[0]) - 96 # a - h is changed to integer 1 - 8
    i = 9 - int(s[1]) # 1 - 8 is changed to integer 8 - 1
    return i, j    

#print(setPosition('a1'))
#print(setPosition('a1')[0] )
#print(setPosition('a1')[1] )

def getPosition():
    start = input("Select a position: \n")
    if (start[0] not in column) or (start[1] not in row):
        print("Invalid input. Check the position again. i.e. a8, h1, etc\n")
    else:
        return setPosition(start)
#    end = input("Select a destination of selected piece ")
#    if (end[0] not in column) or (end[1] not in row):
#        print("Invalid input. Check the destination again. i.e. a8, h1, etc")    
#    return 



def movePawn(m, i, j, ii, jj):
    if m[ii][jj] == 0: # Only movement
        if m[ii][jj-1] in [0, 1]:
            if j == jj and ( (ii - i) == 1 or ( (ii - 1) == 2 and i == 1 ) ):   # 백일 경우는 여기 부호가 반대가 된다!!!!!
                m[ii][jj] = 1
                m[i][j] = 0
            else:
                return -1 ## 과연 이게 될 거인지는 모르겟네요...    
        else:
            return -1 # 중간에 가로막는 것이 있는 경우 
    
    else: # 먹는 경우 
        if (ii - i == 1) and (abs(j-jj) == 1):  # 대각선으로 먹음     ## 백인 경우 여기 i 뺄셈 부호가 반대가 된다!!! 
            m[ii][jj] = 1
            m[i][j] = 0
            #blackcount[ m[ii][jj] ] += 1  # 도착 칸에 있던 기물의 카운트를 +1  
        else:
            return -1 

def moveRook(m, i, j, ii, jj):
    if (i == ii) or (j == jj):
        if (i == ii) and jj - j > 0:
            for k in range(j + 1, jj):
                if m[i][k] != 0:
                    return -1
        elif (i == ii) and jj - j < 0:
            for k in range(j - 1, jj, -1):
                if m[i][k] != 0:
                    return -1
        elif (j == jj) and ii - i > 0:
                for k in range(i + 1, ii):
                    if m[k][j] != 0:
                        return -1
        elif (j == jj) and ii - i < 0:
                for k in range(i - 1, ii, -1):
                    if m[k][j] != 0:
                        return -1  
    else:
        return -1

def moveKnight(m, i, j, ii, jj):
    if (abs(ii-i) == 2 and abs(jj-j) == 1) or (abs(ii-i) == 1 and abs(jj-j) == 2):
        m[ii][jj] = 3
        m[i][j] = 0
    else:
        return -1

def moveBishop(m, i, j, ii, jj): # 4가지 경우 
    if abs(ii-i) == abs(jj-j):
        if (ii - i > 0) and (jj - j > 0):
            for k in range(ii - i - 1):
                if m[i + k + 1][j + k + 1] != 0:
                    return -1
        elif (ii - i > 0) and (jj - j < 0):
            for k in range(ii - i - 1):
                if m[i + k + 1][j - k - 1] != 0:
                    return -1
        elif (ii - i < 0) and (jj - j > 0):
            for k in range(jj - j - 1):
                if m[i - k - 1][j + k + 1] != 0:
                    return -1
        elif (ii - i < 0) and (jj - j < 0):
            for k in range(i - 1, ii, -1):
                if m[k][k] != 0:
                    return -1
        else:
            m[ii][jj] = 4
            m[i][j] = 0
    else:
        return -1

def moveQueen(m, i, j, ii, jj):
    a = moveRook(m, i, j, ii, jj)
    b = moveBishop(m, i, j, ii, jj)
    if (a == -1) and (b == -1):
        return -1
    
def moveKing(m, i, j, ii, jj): # 1칸만 움직임 가능한데, 
    if abs(i - ii) <= 1 and abs(j - jj) <= 1:
        m[ii][jj] = 4
        m[i][j] = 0
    else:
        return -1

def findCheck(m):
    check = [[0 for col in range(8)] for row in range(8)]
    iKing = 0
    jKing = 0
    
    for k in range(8):
        for l in range(8):  
            
            if m[k][l] == 1: 
                try:
                    check[k+1][l+1] += 1
                except:
                    pass
                try:
                    check[k+1][l-1] += 1     ## 흑백이라면!?!!?!?!
                except:
                    pass
            elif m[k][l] == 2: # Rook
                check[k][:] += 1
                check[:][l] += 1
                check[k][l] -= 2
            elif m[k][l] == 3: # Knight
                try:
                    check[k+2][l+1] += 1
                except:
                    pass
                try:
                    check[k+2][l-1] += 1
                except:
                    pass
                try:
                    check[k-2][l+1] += 1
                except:
                    pass
                try:
                    check[k-2][l-1] += 1
                except:
                    pass


                try:
                    check[k+1][l+2] += 1
                except:
                    pass
                try:
                    check[k+1][l-2] += 1
                except:
                    pass
                try:
                    check[k-1][l+2] += 1
                except:
                    pass                   
                try:    
                    check[k-1][l-2] += 1
                except:
                    pass

            elif m[k][l] == 4: # Bishop
                for a in range(1, 8):
                    try:
                        check[k+a][l+a] += 1
                    except:
                        pass
                    try:
                        check[k+a][l-a] += 1
                    except:
                        pass
                    try:
                        check[k-a][l+a] += 1
                    except:
                        pass
                    try:
                        check[k-a][l-a] += 1
                    except:
                        pass
            
            elif m[k][l] == 5: # Queen
                check[k][:] += 1
                check[:][l] += 1
                check[k][l] -= 2
                for a in range(1, 8):
                    try:
                        check[k+a][l+a] += 1
                    except:
                        pass
                    try:
                        check[k+a][l-a] += 1
                    except:
                        pass
                    try:
                        check[k-a][l+a] += 1
                    except:
                        pass
                    try:
                        check[k-a][l-a] += 1
                    except:
                        pass
            
            elif m[k][l] == 6: # King
                try:
                    check[k-1][l-1] += 1
                except:
                    pass
                try:
                    check[k-1][l] += 1
                except:
                    pass
                try:
                    check[k-1][l+1] += 1
                except:
                    pass

                try:
                    check[k][l-1] += 1
                except:
                    pass
                try:
                    check[k][l+1] += 1
                except:
                    pass
                
                try:
                    check[k+1][l-1] += 1
                except:
                    pass
                try:
                    check[k+1][l] += 1
                except:
                    pass
                try:
                    check[k+1][l+1] += 1
                except:
                    pass
                
                iKing = k # Save king index 
                jKing = l

    
    countNearKing = 1
    try:
        countNearKing *= check[iKing-1][jKing-1] 
    except:
        pass
    try:
        countNearKing *= check[iKing-1][jKing] 
    except:
        pass
    try:
        countNearKing *= check[iKing-1][jKing+1] 
    except:
        pass

    try:
        countNearKing *= check[iKing][jKing-1] 
    except:
        pass
    try:
        countNearKing *= check[iKing][jKing+1] 
    except:
        pass
    
    try:
        countNearKing *= check[iKing+1][jKing-1] 
    except:
        pass
    try:
        countNearKing *= check[iKing+1][jKing] 
    except:
        pass
    try:
        countNearKing *= check[iKing+1][jKing+1] 
    except:
        pass
                
    
    if countNearKing == 0:
        print("Checkmate !")

    elif check[iKing][jKing] == 1: 
        print("Check! ")
 
def findPromotion(m, i, j, ii, jj):
    if m[jj][jj] == 1 and ii == 7:  ## 흑백!!!
        print("Pawn is arrived at the end of the board.")
        promotion = int(input("Choose promotion\nSelect one following number - 1. Pawn (Not change)  2. Rook  3. Knight  4. Bishop  5. Queen \n : "))
        if promotion == 1:
            pass
        elif promotion == 2:
            m[ii][jj] = 2
        elif promotion == 3:
            m[ii][jj] = 3
        elif promotion == 4:
            m[ii][jj] = 4
        elif promotion == 5:
            m[ii][jj] = 5
        else:
            print("Invalid number. Nothing to promote.")

                        
                    
                    
                    


    




'''
+  Black
-  White

0  Empty 
1  Pawn
2  Rook
3  Knight
4  Bishop
5  Queen
6  King 


Initial state 
   A  B  C  D  E  F  G  H
8  2  3  4  5  6  4  3  2 
7  1  1  1  1  1  1  1  1 
6  0  0  0  0  0  0  0  0
5  0  0  0  0  0  0  0  0
4  0  0  0  0  0  0  0  0
3  0  0  0  0  0  0  0  0
2  -1 -1 -1 -1 -1 -1 -1 -1 
1  -2 -3 -4 -5 -6 -4 -3 -2

State matrix

1  1  1  1  1  1  1  1 
0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0
-1 -1 -1 -1 -1 -1 -1 -1 
-2 -3 -4 -5 -6 -4 -3 -2

Column  A B C D E F G H 
Index   0 1 2 3 4 5 6 7

Row     8 7 6 5 4 3 2 1 
Index   0 1 2 3 4 5 6 7 
'''
state = []
'''
# Insert 
start_position = input("Select a piece which you want to move - start: ")


end_position = input("Select a destination of selected piece ")



while(on = 1)
    
    ask
    movement()
'''

showPosition(test)
valid = 0
m = test
while(1):
    print("Select a piece which you want to move\n")
    (i, j) = getPosition()
    
    print("Select a destination\n")
    (ii, jj) = getPosition()
    
    if m[i][j] == 0:
        print("You choose an empty place. Try again.\n")    
        continue
    elif i == ii and j == jj:
        print("You choose two same positions. Try again.\n")    
        continue        
    print("m i j", m[i][j])
    print("m ii jj", m[ii][jj])
    getPiece = m[i][j] * m[ii][jj]

    if m[i][j] == 1: # Pawn
        valid = movePawn(m, i, j, ii, jj)

    elif m[i][j] == 2:
        valid = moveRook(m, i, j, ii, jj)

    elif m[i][j] == 3:
        valid = moveKnight(m, i, j, ii, jj)

    elif m[i][j] == 4:    
        valid = moveBishop(m, i, j, ii, jj)
    
    elif m[i][j] == 5:
        valid = moveQueen(m, i, j, ii, jj)

    elif m[i][j] == 6:
        valid = moveKing(m, i, j, ii, jj)


    if valid == -1: 
        print("Invalid movement. Try again")
        continue
    elif getPiece >= 0: # 먹는경우 
        print("Invalid movement. You can not catch your piece. Try again")
        continue

    findCheck(m)
    findPromotion(m, i, j, ii, jj)





