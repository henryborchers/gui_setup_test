__author__ = 'California Audio Visual Preservation Project'
import sys
if sys.version_info > (3,0):
    from tkinter import *
else:
    from Tkinter import *
def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "--test":
            print("Test successful")
            exit()
        else:
            exit(-1)
    if len(sys.argv) > 2:
        exit()
    elif len(sys.argv) == 1:
        print("Hello")
        root = Tk()
        # w = tkinter.Label(root, text="Hello World")
        w = Button(root, text="Close Me", command=callback)
        w.pack()
        root.mainloop()

def callback():
    print("Closing")
    exit()

if __name__ == '__main__':
    main()