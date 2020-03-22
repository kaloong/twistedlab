from six.moves import tkinter
import sys

class Dashboard(tkinter.Frame,object):
    def __init__(self, root):
        super(Dashboard,self).__init__(root)
        self.pack()
        self.check1butt=tkinter.Button(self, text="Check 1", command=self.check1)
        self.check1butt.pack(side="top")
    def check1(self):
        print("Check 1")

if len(sys.argv) < 2:
    print("Use -s for server or -c for client.")
    sys.exit(2)
else:
    if sys.argv[1] == "-s":
        print("Run as server")
    elif sys.argv[1] == "-c":
        print("Run as client")
        root=tkinter.Tk()
        App=Dashboard(root)
        root.mainloop()
