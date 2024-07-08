# dispImageKadai01.py

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
    lbl2 = tk.Label(text=path, font=("Helvetica", 16))
    lbl2.pack()

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        # fpathをprint()でシェルに出力
        print(fpath)

root = tk.Tk()

root.geometry("500x490") # ウインドウサイズの調整

lbl1 = tk.Label(text="🎨画像表示アプリ バージョン2.0🎨", font=("Helvetica", 16))
btn = tk.Button(text="ファイルを開く",font=("Helvetica", 16), command = openFile)
lbl1.pack()
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()
