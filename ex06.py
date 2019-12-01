#金額を入力するとその金額を出来るだけ少ない枚数の貨幣を使って支払えるように貨幣の枚数を数えるプログラムを書きなさい。貨幣は、{１万円札、五千円札、千円札、五百円玉、百円玉、五十円玉、十円玉、五円玉、一円玉}とする（余り使わないので２千円札は除く）。

money = int(input("金額(円) >"))

print(money,"円")

maisu =money // 10000
money = money % 10000
print("一万円札= ",maisu,"枚")

maisu =money // 5000
money = money % 5000
print("五千円札= ",maisu,"枚")

maisu =money // 1000
money = money % 1000
print("千円札　= ",maisu,"枚")

maisu =money // 500
money = money % 500
print("五百円玉= ",maisu,"枚")

maisu =money // 100
money = money % 100
print("百円玉　= ",maisu,"枚")

maisu =money // 50
money = money % 50
print("五十円玉= ",maisu,"枚")

maisu =money // 10
money = money % 10
print("十円玉　= ",maisu,"枚")

maisu =money // 5
money = money % 5
print("五円玉　= ",maisu,"枚")

print("一円玉　= ",money,"枚")
