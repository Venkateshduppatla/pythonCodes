# First Gui program. 

import tkinter as tk
r = tk.Tk()
r.title('Chat Box')
button = tk.Button(r, text='Cancel', width=25, command=r.destroy)
button.pack()
r.mainloop()