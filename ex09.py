#練習09 うるう年の判定 (ex09.py)
#うるう年というのは、四年に一度、二月が29日まである年のことをいうと思われていますが、正確にはもっと複雑です。西暦の年に対して、
#年が400で割り切れるなら、うるう年です。
#そうではなくて年が100で割り切れるならば、うるう年ではありません。
#そうでもなくて年が4で割り切れるならば、うるう年です。


year = int(input("西暦で年を入力して下さい >"))

if year % 400 == 0:
    print(year,"年はうるう年です")
elif year % 100 == 0:
    print(year,"年はうるう年ではありません")
elif year % 4 == 0:
    print(year,"年はうるう年です")
else:
    print(year,"年はうるう年ではありません")