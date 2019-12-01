#練習11 ジャンケンするプログラム (ex11.py)

import random

print("じゃんけんポン!")
player = int(input("あなたは？(0:グー, 1:チョキ, 2:パー) >"))
if player == 0:
    hand = "グー"
elif player == 1:
    hand = "チョキ"
elif player == 2:
    hand = "パー"
else:
    print("0,1,2のいずれかを入力して下さい")

comp = random.randint(0,2)
if comp == 0:
    cp_hand = "グー"
elif comp == 1:
    cp_hand = "チョキ"
elif comp == 2:
    cp_hand = "パー"

if player == comp:
    battle = "おあいこです（・ω・）"
elif (player == 0 and comp == 1) or (player == 1 and comp == 2) or (player == 2 and comp == 0):
    battle = "あなたの勝ちです(｀・ω・´)"
elif (player == 0 and comp == 2) or (player == 1 and comp == 0) or (player == 2 and comp == 1):
    battle = "あなたの負けです(´・ω・`)"

print("わたしは"+str(cp_hand)+"。あなたは"+str(hand)+"。"+str(battle))

