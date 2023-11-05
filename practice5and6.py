### コレクション練習問題 (10/31)

# 練習問題1
# 西暦を入力すると干支を教えてくれるプログラムを作成してください。
# （干支の条件から調べてください。十二支で良いです。）

eto = ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未"]
year = int(input("西暦を入力してください>>>"))
# print(f"{1994%12}は戌")

index = year % 12
print(f"{eto[index]}年です")


# 練習問題2
# キーボードから国語算数理科社会英語の各教科の点数を入力させ、合計点と平均点を出力するプログラムを作成してください。
# 各教科ごとの点数は出力しないでよいです。

sub = ["国語", "算数", "理科", "社会", "英語"]

list = []
for i in sub:
    list.append(int(input(f"{i}の点数は?")))

print(f"合計点は{sum(list)}です")
print(f"平均点は{sum(list) / len(list)}です")


# 練習問題3
# 以下のリストを用いて、以下の問題に答えなさい。
sub = ["国語", "算数", "理科", "社会"]
taro = [88, 91, 92, 100]
jiro = [47, 51, 62, 31]
saburo = [98, 38, 87, 85]
hanako = [97, 99, 85, 100]
haruko = [96, 85, 40, 85]
natsuko = [87, 73, 73, 70]

# ①生徒ごとの最高点、最低点、合計点を求めて出力してください。

name_list = {
    "taro": taro,
    "jiro": jiro,
    "saburo": saburo,
    "hanako": hanako,
    "haruko": haruko,
    "natsuko": natsuko,
    }

for n, l in name_list:
    print(f"{n}の最高点は{max(l)}, 最低点は{min(l)}, 合計点は{sum(l)}")


# ②科目ごとの最高点、最低点、平均点を求めて出力してください。

for i in zip(sub, taro, jiro, saburo, hanako, haruko, natsuko):
    scores = list(i)
    scores_new = scores[1:]
    print(f"{scores[0]}の最高点は{max(scores_new)}、最低点は{min(scores_new)}、平均点{sum(scores_new)/len(scores_new)}")


# ③リストに英語の項目を追加し、キーボードから入力したデータを要素に追加
# してください。英語の最高点、最低点、平均点を求めて出力してください。

new_sub = input("追加する教科を入力してください>>>")
sub.append(new_sub)

for n, l in name_list.items():
    new_score = int(input(f"{n}さんの{new_sub}の点数は？>>>"))
    l.append(new_score)

for i in zip(sub, taro, jiro, saburo, hanako, haruko, natsuko):
    scores = list(i)
    if scores[0] == new_sub:
        scores_new = scores[1:]
        print(f"{scores[0]}の最高点は{max(scores_new)}、最低点は{min(scores_new)}、平均点{sum(scores_new)/len(scores_new)}")


# 練習問題4★★
# コレクションを使ってじゃんけんプログラムを作成しましょう。
# 条件分岐や繰り返しを使わないで作成して下さい。
# 学習前ですが、ランダムに数を輩出する仕組みとして標準ライブラリのrandintという機能を使います。

# 下記をそのままコピーしてください。
###
# import random as r
# num = r.randint(0,2)
# print(num)
###

import random as r
num = r.randint(0,2)
# print(num)
scp = ["ぐー", "ちょき", "ぱー"]
result = ["あなたの勝ち", "あなたの負け", "あいこ"]
# winner = [{あなたの手、勝敗}]scp0=ぐー,1＝ちょき,2＝ぱー
winner = [
    {"ぐー": 2, "ちょき": 1, "ぱー": 0},
    {"ぐー": 0, "ちょき": 2, "ぱー": 1},
    {"ぐー": 1, "ちょき": 0, "ぱー": 2},
    ]

te = input("最初はぐー！じゃんけんぽん！(ぐー、ちょき、ぱー)>>>")

print(f"あなたは{te}、私は{scp[num]}")
res = winner[num][te]
print(result[res])
