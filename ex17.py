#借金をして月々、定額を返済していくと借金はどうなっていくのかを調べるプログラムを作成しよう。
# 借金の金額と、利息の年利率(%)、月々の返済額を入力すると、毎月、借金がなくなるまで月数と借金の金額を
# 表示するものとする。月々の借金は、借金の利息年利率/12（月割り）分増加するが、返済分だけ減る。

dept = int(input("借金 >"))
nenri = float(input("年利率（％） >"))
hensai = int(input("返済額 >"))
total = 0
month = 0

while dept > hensai:
    month += 1
    dept = dept * (1 + nenri/12/100) - hensai

    #print(str(month)+"月: 返済額 ",hensai," 円 残り "+int(dept)+"円")
    print(str(month)+'月: 返済額',hensai,'円','残り',int(dept),sep=' ')
    total += hensai
month += 1
dept = dept * (1 + nenri/12/100)
total += dept
#print(str(month)+"月: 返済額 ",int(dept)," 円これで完済。 返済総額: "+int(total)+"円",sep='')
print(str(month)+'月: 返済額',int(dept),'円','これで完済。','返済総額: ',int(total),'円',sep=' ')
