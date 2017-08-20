from curses import wrapper
import curses
import time


def update_server_list(pad, server_list):
    for i in range(0, min(len(server_list), 10)):
        pad.addstr(i, 1, server_list[i])


def main(stdscr):
    server_list_pad = curses.newpad(11, 100)

    while 1:
        stdscr.clear()
        update_server_list(server_list_pad, ["Developers", "</dd>"])

        stdscr.refresh()
        server_list_pad.refresh(0, 0, 0, 0, 80, 11)
        curses.doupdate()

        time.sleep(1)

wrapper(main)
