#健康のために肥満度をチェックしてみましょう。身長と体重を入力してあなたの肥満度（BMI＝体重(kg)÷身長(m)の二乗）を計算するプログラムを作成し、判定基準に従って、18.5未満→やせ、18.5〜25未満→標準、25〜30未満→肥満、30以上→高度肥満という判定を返すプログラムを作りなさい。
#あなたは「標準」です。

height = float(input("身長をm単位で入力して下さい> "))
weight = float(input("体重をkg単位で入力して下さい> "))
bmi = float(weight/pow(height,2))

print("BMI = ",bmi)

if bmi < 18.5:
    print("あなたは「やせ」です。")
elif 18.5 <= bmi < 25:
    print("あなたは「標準」です。")
elif 25 <= bmi < 30:
    print("あなたは「肥満」です。")
elif 30 < bmi:
    print("あなたは「高度肥満」です。")
else:
    print("error")
