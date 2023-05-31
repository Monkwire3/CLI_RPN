import curses 
import os


print('Welcome to CLIRP: An rpn calculator for your terminal!')

def main(win):
    win.nodelay(True)
    key=''
    win.clear()
    win.addstr('detected key')
    while 1:
        try:
            key = win.getkey()
            win.clear()
            win.addstr('detected key')
            win.addstr(str(key))
            if key == os.linesep:
                break
        except Exception as e:
            pass

curses.wrapper(main)
        
