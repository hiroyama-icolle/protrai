# GUIで動くアプリを作ってみるよtkrensyu.py

import tkinter as tk # まずこの行を書く必要があるよ

root = tk.Tk() #初めのおまじない

root.geometry("300x200") # ウインドウのサイズを決める
root.title("アプリの練習") #　ウインドウのタイトルを決める
lbl = tk.Label(text="Hello World") # いつもの
lbl.pack() # lblを配置させる必要があるよ

root.mainloop() # 終わりのおまじない
