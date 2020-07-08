import Choose
import Game
with open("./Text/example.txt") as f:
    for i in f.readlines():
        lis=i.split(" ")
        if lis[0]=="event_choose":
            print("去做出选择")
            Choose.choose.cho(lis)
        elif lis[0] =="event_game":
            Game.game(int(lis[1]))
        else:
            print(lis[0])
            input()