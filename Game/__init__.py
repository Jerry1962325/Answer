from pygame import *
def game(i):
    if i==1:
        init()
        screen = display.set_mode((500, 200))
        display.set_caption("泡泡茶壶")
        while True:
            for events in event.get():
                if events.type == QUIT:
                    return None
    elif i==2:
        pass