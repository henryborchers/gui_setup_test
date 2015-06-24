__author__ = 'California Audio Visual Preservation Project'
import tkinter

def main():
    print("Hello")
    root = tkinter.Tk()
    # w = tkinter.Label(root, text="Hello World")
    w = tkinter.Button(root, text="Close Me", command=callback)
    w.pack()
    root.mainloop()

def callback():
    print("Closing")
    exit()

if __name__ == '__main__':
    main()