import tkinter as tk
from tkinter import ttk

app = tk.Tk()


def quit_cmd():
    app.quit()


progress_bar = ttk.Progressbar()
progress_bar.grid()
progress_bar.start()

button = ttk.Button(app, text='quit', command=quit_cmd)
button.grid()

app.mainloop()
