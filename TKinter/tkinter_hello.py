from tkinter import *
# Import everything from the tkinter module

root = Tk()
# To initialize TKinter, we have to create a Tk root widget, which is a 
# window with a title bar and other decoration provided by the window
# manager. The root widget has to be created before any other widgets,
# and there can only be one root widget.

w = Label(root, text="Hello TKinter!")
# This contains the Label widget. The first parameter of the Label call
# is the name of the parent window, in our case "root". So our label is
# a chile fo the root widget. The keyword parameter "text" specifies the
# text to be shown.

w.pack()
# The pack method tells Tk to fir the size of the window to the given
# text.

root.mainloop()
# The window will not appear until we enter the Tkinter event loop, and
# will remain in the event loop until the window is closed.
