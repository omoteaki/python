### Lesson4

# 比較演算子
print(3 < 1)   #False
print(1 < 3)   #True

print(1 >= 1)   #True
print(1 > 1)   #False

print(1 == 1)   #True
print(1 == 2)   #False

print(1 != 1)   #False
print(1 != 2)   #True

# if文
# sample1
sale = int(input("売上を入力してください"))

if sale >= 100:
    print("売上は好調です")
print("処理を終了します。")

# sample2
sale = int(input("売上を入力してください"))

if sale >= 100:
    print("売上は好調です")
elif sale >= 50:
    print("売上は普通です")
else:
    print("売上は低調です")

print("処理を終了します。")

# ↑の書き換え
sale = int(input("売上を入力してください"))
# judg = "低調"
# 最初に変数を用意しておいた方が良いと思っていたけど、なくても動いた(他の言語でどうだったか要確認)

if sale >= 100:
    judg = "好調"
elif sale >= 50:
    judg = "普通"
else:
    judg = "低調"

print(f"売上は{judg}です")
print("処理を終了します。")


# 論理演算子
# sample3
sale = int(input("売上を入力して下さい"))
num = int(input("人数を入力して下さい"))

if sale >= 100 and num >= 30:
    earning = "大盛況"
elif sale >= 100:
    earning = "好調"
elif sale >= 50:
    earning = "普通"
else:
    earning = "低調"

print(f"売上は{earning}です")


# for文
# sample4
for i in range(12):
    print(i + 1, "月のデータです")

# ↑書き換え
for i in range(13):
    print(i, "月のデータです")


# while文
# sample5
i = 1
while i <= 12:
    print(f"{i}月のデータです")
    i += 1

# 文のネスト
# sample6
for i in range(5):
    for j in range(3):
        print(f"iは{i}:jは{j}")


# sample7
v = False

for i in range(5):
    for j in range(5):
        if v is False:
            print("*", end="")
            v = True
        else:
            print("-", end="")
            v = False
    print()


#####
# コマンドライン上にオセロの盤面を再現できるのでは？
# i=行の番号
# j=列の番号

for i in range(9):
    for j in range(9):
        # 行と列番号の表示
        if i == 0:
            print(j, end=" ")
        elif j == 0:
            print(i, end=" ")

        # 初期位置
        elif (i == 4 and j == 4) or (i == 5 and j == 5):
            print("W", end=" ")
        elif (i == 4 and j == 5) or (i == 5 and j == 4):
            print("B", end=" ")
        else:
            print("*", end=" ")
    print()

#####


# 練習
# 1
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 2 (出力結果は1と同じ)
for i in range(2, 11, 2):
    print(i)

# 3
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, "\t", end="")
    print()

# 4
for i in range(1, 6):
    print("*" * i)
