import curses 
import os


print('Welcome to CLIRP: An rpn calculator for your terminal!')

def main(win):
    string = ''
    win.nodelay(True)
    key=''
    win.clear()
    win.addstr('Welcome to CLIRP: An rpm calculator for your terminal!')
    while 1:
        try:
            key = win.getkey()
            win.clear()
            win.addstr(string)
            string += key
            if key == os.linesep:
                break
        except Exception as e:
            pass

curses.wrapper(main)
        
