#数字を入力して、1からその数までの棒グラフを順に表示するプログラムを書きなさい。

n = int(input("数字>"))
for j in range(1,n+1) :
    print(str(j)+':',end='')
    for i in range(0,j) :
        print('■',end=' ')
    print() #改行だけ出力
