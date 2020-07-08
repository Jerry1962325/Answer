from tkinter import *
class choose:
    def cho(lis):
        root = Tk()
        for i in range(2, len(lis)-1):
            Button(root, text=lis[i], command=lambda a=lis[i]:click(lis[1],a)).pack()
            def click(N,cho):
                print("你的选择:",cho)
                root.destroy()
                with open("./Text/{0}/{1}.cho".format(lis[1],lis[i])) as f:
                    pass
        mainloop()