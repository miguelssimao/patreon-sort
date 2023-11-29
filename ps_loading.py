from time import sleep
from itertools import cycle
from sys import stdout as terminal

done, first, bypass, bytype, bytier, load, final = (False for _ in range(7))


def loading():
    for c in cycle(["|", "/", "-", "\\"]):
        if done:
            break
        if first:
            text = "Analyzing the url... "
        if bypass:
            text = "Bypassing cookies... "
        if bytype:
            text = "Filtering by type... "
        if bytier:
            text = "Filtering by tier... "
        if load:
            text = "Loading all posts... "
        if final:
            text = "Done. Please wait... "
        terminal.write("\r" + text + "" + c)
        terminal.flush()
        sleep(0.1)
    terminal.flush()
