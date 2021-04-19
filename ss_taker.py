import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()

canvas_1 = tk.Canvas(root, width=300, height=300)
canvas_1.pack()


def takeScreenshot():
    my_screenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    my_screenshot.save(save_path)


myButton = tk.Button(text="Take screenshot", command=takeScreenshot, font=10)
canvas_1.create_window(150, 150, window=myButton)

root.mainloop()
