#! python3
# mcbDelete.pyw - saves, loads, and deletes pieces of text to the clipboard
# usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard
#        py.exe mcb.pyw delete <keyword> - deletes keyword from the shelf
#        py.exe mcb.pyw delete - deletes all keywords
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcbShelf[sys.argv[2]] = ''
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
print(sys.argv[1])
# todo: list keywords and load content
mcbShelf.close()
