# Tutorial from www.python-course.eu/tkinter_labels.php

from tkinter import *
# As has already been mentioned, labels can contain text and images. The
# following example contains two labels, one with a text and the other
# one with an image.

root = Tk()
logo = PhotoImage(file="../images/python_logo.gif")
w1 = Label(root, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM formats are supported,
but an interface exists to allow additional image file formats to be
added easily."""

w2 = Label(root,
		   justify=LEFT,
		   padx = 10,
		   text=explanation).pack(side="left")
# The "justify" parameter can be used to justify a text on the LEFT,
# RIGHT or CENTER. padx can be used to add additional horizontal padding
# around a text label. The defual padding is 1 pixel. pady is similar
# for vertical padding.

root.mainloop()
