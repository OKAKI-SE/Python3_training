#３つの数を入力し、数を昇順に並べ替えてから出力するプログラムを作成してください。

num1 = input("数1 >")
num2 = input("数2 >")
num3 = input("数3 >")

x = [num1,num2,num3]

print(sorted(x))
#print(sorted(x, reverse=True)) #降順

#list.sort(x)
#print(x)
#list.sort(x, reverse=True) #降順

 