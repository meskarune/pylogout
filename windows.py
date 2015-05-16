#!/usr/bin/python2

from Xlib import display, X

display = display.Display()
screen = display.screen()
root = screen.root
tree = root.query_tree()
wins = tree.children

for win in wins: 
    print win.get_wm_name()
