# s24000　entry_kadai.py
# エントリーウィジェットで受け付けた金額を税込み(10%)価格としてラベル出力するようにしてください
# 続きはこのコードをアレンジして各自作成してみてください　172.16.41.158

import tkinter as tk # tkinterをtkと略して使用する

def dispLabel():
    # entryメソッドを使用して入力を受け付け変数aに格納
    a = entry.get()
    # ログの出力
    print(f"aは{type(a)}")
    #lbl.config(text=f"{a}さんこんにちは")
    lbl.config(text=f"税込み金額{int(a)*1.1}円")

root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200") # 画面の大きさを決める

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
