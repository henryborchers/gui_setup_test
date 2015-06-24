__author__ = 'California Audio Visual Preservation Project'
import sys
if sys.version_info > (3,0):
    from tkinter import *
else:
    from Tkinter import *
def main():
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