# s24000
# BMI値計算プログラム ファイル名は「bmi.py」

h = float(input("身長何cmですか？")) / 100.0
w = float(input("体重何kgですか？"))

bmi = w / (h * h)
print("あなたのBMI値は、",bmi,"です。")
