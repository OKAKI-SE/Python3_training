#分かんなくて答え見たやつ
#255以下の10進数を入力して、それを８桁の２進数で表示するプログラムを書きなさい。

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

x10 = int(input("数字を10進数で入力して下さい >"))
x2 = Base_10_to_n(x10, 2)
print(x2)
