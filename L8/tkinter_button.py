# install tkinter:
# sudo apt-get install python3-tk
# restart PyCharm
# http://younglinux.info/tkinter/widget.php

from tkinter import *

root = Tk()

# create object
but = Button(root,
             text="Это кнопка",  # надпись на кнопке
             width=30, height=5,  # ширина и высота
             bg="white", fg="blue")  # цвет фона и надписи

but.pack()
root.mainloop()