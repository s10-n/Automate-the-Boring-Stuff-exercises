from string import ascii_lowercase
startingBoard = {'1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bking', '1e': 'bqueen', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
                   '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
                   '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
                   '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking', '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook'}
endgameBoard = {'1h': 'bpawn',
                '5c': 'wqueen',
                '2g': 'bbishop',
                '5h': 'bqueen',
                '3e': 'wking'}
def isValidChessBoard(board):
    validNumberOfPieces = True
    validSpaceNumber = True
    validSpaceLetter = True
    validPieceColour = True
    validPieceName = True
    piecesPerPlayer = {'black':{'pawn':0,'rook':0,'knight':0,'bishop':0,'king':0,'queen':0},
                       'white':{'pawn':0,'rook':0,'knight':0,'bishop':0,'king':0,'queen':0}}
    pieceMaximums = {'pawn':8,'rook':2,'knight':2,'bishop':2,'king':1,'queen':1}
    def allocatePieceName(c): # counts pieces per player, takes a string
        try:
            if c == 'b': # determines piece colour
                colour = 'black'
            elif c =='w': # determines piece colour
                colour = 'white'
            else:
                return False
            if piece[1:] in piecesPerPlayer[colour]: # counts pieces per player
                    piecesPerPlayer[colour][piece[1:]] += 1
            if piecesPerPlayer[colour][piece[1:]] > pieceMaximums[piece[1:]]: # checks if pieces per player is too high
                return False
        except KeyError:
            return False
    for space in board.keys(): # test that all spaces are valid
        if int(space[0]) == 0: # tests space number
            validSpaceNumber = False
            break
        elif int(space[0]) > 8:
            validSpaceNumber = False
            break
        if ascii_lowercase.find(space[1]) > 7: # tests space letter
            validSpaceLetter = False
            break
    for piece in board.values(): # test that all pieces are valid
        if allocatePieceName(piece[0]) == False:
            validNumberOfPieces = False
            break
        if piece[1:] not in piecesPerPlayer['black']: # tests piece name
            validPieceName = False
            break
    if validNumberOfPieces == True and validSpaceNumber == True and validSpaceLetter == True and validPieceColour == True and validPieceName == True:
        return True
    else:
        return False
print(isValidChessBoard(startingBoard))
print(isValidChessBoard(endgameBoard))