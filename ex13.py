#練習13 べき乗計算 (ex13.py)
#1以上の整数を入力し、その数までのべき乗を計算するプログラムを作成せよ。

num = int(input("数 >"))
beki = pow(num,num)
#beki = num ** num #こっちでもいける

print(num,"! = ",beki,sep='')
