#練習08 整数曜日変換 (ex08.py)
#0から6までの整数を入力して、それぞれ、0ならば「日曜」、1ならば「月曜」、...と
# 結果を返すプログラムを書きなさい。但し、0〜6の数以外の数値が入力された場合には、「0から6までの数を入力してください」とメッセージを返すようにしなさい。
#実行結果
#数(0-6)> 5
#金曜日

number = int(input("Please enter a number 0-6."))

if number == 0:
    print("Sunday")
elif number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
else:
    print("Please enter a number between 0 and 6")
