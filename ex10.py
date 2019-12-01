#練習10 あなたの誕生日は何曜日？ (ex10.py)
#Zëllerの公式(1887)という公式を使うと、1582年10月15日以降の日付から曜日を計算することができます。
# 整数(int)として年をyear、月をmonth、日をdayとした時、曜日(weekday)は
#weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7
#という式で計算できます。曜日は整数として0が日曜、1が月曜、...、6が土曜となります。
#但し、1月と2月はそれぞれ前の年の13月、14月として計算する必要があります。
# 例えば、2000年1月というのは上の計算式では、1999年13月として計算しなければなりません。
#自分の誕生日を入力して、生まれた日が何曜日かを調べなさい。


year = int(input("年 >"))
month = int(input("月 >"))
day = int(input("日 >"))

weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7

if weekday == 0:
    week = "日"
elif weekday == 1:
    week = "月"
elif weekday == 2:
    week = "火"
elif weekday == 3:
    week = "水"
elif weekday == 4:
    week = "木"
elif weekday == 5:
    week = "金"
elif weekday == 6:
    week = "土"

print(year,"年",month,"月",day,"日は",week,"曜日です。",sep='')

