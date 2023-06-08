import curses 
import os


print('Welcome to CLIRP: An rpn calculator for your terminal!')
def buildOverlay(win):
    win.nodelay(True)
    # win.clear()
    win.addstr('OVERLAY')
    win.addstr('=' * 100)

def addPad():
    pad = curses.newpad(100, 100)
    # These loops fill the pad with letters; addch() is
    # explained in the next section
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

    # Displays a section of the pad in the middle of the screen.
    # (0,0) : coordinate of upper-left corner of pad area to display.
    # (5,5) : coordinate of upper-left corner of window area to be filled
    #         with pad content.
    # (20, 75) : coordinate of lower-right corner of window area to be
    #          : filled with pad content.
    pad.refresh( 0,0, 5,5, 20,75)


def renderHeader(win):
    r, c = win.getmaxyx()
    win.addstr(0, 0, f"{'===' * ((r // 2) - 10)} <HEADER> {'===' * ((r // 2) - 10)}") 



def main(win):
    string = ''
    win.nodelay(True)
    key=''
    win.clear()
    win.addstr(0, 0, 'Welcome to CLIRP: An rpn calculator for your terminal!\n')
    win.addstr('Press any key to start.')
    while True:
        try:
            key = win.getkey()
            string += key
            win.clear()
            win.addstr(10, 10, string)
            renderHeader(win)
        except Exception as e:
            pass

curses.wrapper(main)
        
