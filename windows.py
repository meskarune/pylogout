#!/usr/bin/python2

#from Xlib import display, X

#display = display.Display()
#screen = display.screen()
#root = screen.root
#tree = root.query_tree()
#wins = tree.children

#for win in wins: 
#    print win.get_wm_name()

import xcffib
import xcffib.xproto

display = xcffib.connect()
screen = display.get_setup().roots[0]
root = screen.root
tree = root.query_tree()
wins= tree.children

for win in wins:
    print win.get_wm_name()
