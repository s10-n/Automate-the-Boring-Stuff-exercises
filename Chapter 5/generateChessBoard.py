import string
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
chessBoard = {}
for number in range(1,9):
    for letter in range(0,8):
        chessBoard[str(number) + string.ascii_lowercase[letter]] = ''

print(chessBoard)
r.clipboard_append(chessBoard)
r.update()
r.destroy()
#{'1a':' ','1b':' ','1c':' ','1d':' ','1e':' ','1f':' ','1g':' ','1h':' ',