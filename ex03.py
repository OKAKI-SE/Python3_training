#健康のために肥満度をチェックしてみましょう。
#身長と体重を入力してあなたの肥満度（BMI＝体重(kg)÷身長(m)の二乗）を計算するプログラムを作成し、計算結果を確かめてください。
#判定基準が18.5未満→やせ、18.5〜25未満→標準、25〜30未満→肥満、30以上→高度肥満となっているようです。

height = float(input("身長をm単位で入力して下さい>"))
weight = float(input("体重をkg単位で入力して下さい>"))
BMI = weight / pow(height,2)

print("あなたのBMIは",round(BMI,2))

if BMI < 18.5:
    print("やせ")
elif 18.5 <= BMI < 25:
    print("標準")
elif 25 <= BMI < 30:
    print("肥満")
elif 30 < BMI:
    print("高度肥満")