### Lesson5

# リストの作り方
scores = [22, 12, 44]
# カンマで区切る

# sample1
sale = [80, 60, 22, 50, 75]
print(sale)

# sample2
print(sale[0])
print(sale[1])
print(sale[2])
print(sale[3])
print(sale[4])
print(f"リストの長さは、{len(sale)}です")

# sample3
sale = [80, 60, 22, 50, 75]
for s in sale:
    print(s)
print(f"リストの長さは、{len(sale)}です")


### 指定した値がどこに格納されてるか調べる方法は？
# お試し
sale = [80, 60, 22, 50, 75, 22]
num = 22   #どこに入っているか調べたい値

for i in range(len(sale)):
    # print(i, end=":")
    # print(sale[i])
    if sale[i] == 22:
        print(f"ここに入ってます{i}")

###

# sample4
sale = [80, 60, 22, 50, 75]

i = int(input("何番のデータを変更しますか？"))
num = int(input("変更後のデータを入力してください。"))

print(f"{i}番のデータ{sale[i]}を変更します。")

sale[i] = num

print(f"{i}番のデータは{sale[i]}に変更されました。")


# sample5
sale = [80, 60, 22, 50, 75]
print(f"現在のデータは{sale}です。")

print("末尾に100を追加します。")
sale.append(100)
print(f"現在のデータは{sale}です。")

print("sale[2]に25を挿入します。")
sale.insert(2,25)
print(f"現在のデータは{sale}です。")


# 100以下の値をリストから削除する
for i in scores:
    if i <= 100:
        scores.remove(i)


# sample6
sale = [80, 60, 22, 50, 75]
print(f"現在のデータは{sale}です。")

print("先頭のデータを削除します")
del sale[0]
print(f"現在のデータは{sale}です。")

print("22を削除します。")
sale.remove(22)
print(f"現在のデータは{sale}です。")


# sample7
data1 = [1, 2, 3, 4, 5]
data2 = data1

print(f"data1は{data1}です")
print(f"data2は{data2}です")

data1[0] = 10

print("date1を変更します。")
print(f"data1は{data1}です")
print(f"data2は{data2}です")
# data1を変更するとdata2も変更されることに注意


# コピーするけど、片方だけ変更したいときは、
# 新しくリストを作る
# sample8
data1 = [1, 2, 3, 4, 5]
# list関数を使う場合
# data2 = list(data1)
# copyメソッドを使う場合
data2 = data1.copy()

print(f"data1は{data1}です")
print(f"data2は{data2}です")

data1[0] = 10

print("date1を変更します。")
print(f"data1は{data1}です")
print(f"data2は{data2}です")


# リストの連結
# sample9
sale1 = [1, 2, 3, 4, 5, 6]
print(f"上半期のデータは{sale1}です")
sale2 = [7, 8, 9, 10, 11, 12]
print(f"下半期のデータは{sale2}です")

ysale = sale1 + sale2

print(f"年間のデータは{ysale}です")


# スライス
# sample10
ysale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"年間のデータは{ysale}です")

sale1 = ysale[0:6]
print(f"上半期のデータは{sale1}です")
sale2 = ysale[6:]
print(f"下半期のデータは{sale2}です")
sale3 = ysale[::2]
print(f"一か月おきのデータは{sale3}です")
sale4 = ysale[::-1]
print(f"逆順のデータは{sale4}です")

print(f"年間のデータは{ysale}です")

# スライスへの代入もできる
print("上半期のデータを差し替えます")
ysale[:6] = [0, 0, 0, 0, 0, 0]
print(f"年間のデータは{ysale}です")


# sample11
data = [1, 2, 3, 4, 5]
print(f"現在のデータは{data}です")

print("data[::-1]をfor文で処理します")
for d in data[::-1]:
    print(d)
print(f"data[::-1]は{data}です")
print(f"現在のデータは{data}です")
# スライスしても元のリスト自体が変更されるわけではない

print("reversed(data)をfor文で処理します")
for d in reversed(data):
    print(d)
print(f"reversed(data)は{reversed(data)}です")

print("data.reverse()を処理します")
data.reverse()
print(f"現在のデータは{data}です")


##### タプル #####

tp = (1, 2, 3, 4, 5)

###


# sample12
city = ["東京", "名古屋", "大阪", "京都"]
sale = [80, 60, 22, 50, 75]

print(f"都市名データは{city}です")
print(f"売上データは{sale}です")

print("データを組み合わせます")

for d in zip(city, sale):
    print(d)

print("データとインデックスを組み合わせます")

for d in enumerate(city):
    print(d)


## リストの表記の仕方、改行する場合
list = [
    1,
    2,
    3,
    4,   #最後の要素にもカンマをつける＝＞カンマのつけ忘れ防止
]


# sample13
city = ["東京", "名古屋", "大阪", "京都"]
sale = [80, 60, 22, 50, 75]

print(f"都市名データは{city}です")
print(f"売上データは{sale}です")

print("データを組み合わせます")

for d in zip(city, sale):
    print(d)

print("データを分解します")

for c, s in zip(city, sale):
    print(f"都市名は{c}売上は{s}")


# リスト内包表記
# sample14
data = [1, 2, 3, 4, 5]
print(f"現在のデータは{data}です")

ndata = [n*2 for n in data if n!=3]
print(f"新しいデータは{ndata}です")


# sample15
sale = [80, 60, 22, 50, 75]

print(f"現在のデータは{sale}です")
print(f"最大のデータは{max(sale)}です")
print(f"最小のデータは{min(sale)}です")
print(f"データの合計は{sum(sale)}です")
print(f"ソートされたデータは{sorted(sale, reverse=True)}です")


# sample16
data = [
    ["東京", 32, 25],
    ["名古屋", 28, 21],
    ["大阪", 27, 21],
    ["京都", 26, 19],
    ["福岡", 27, 22],
]

print(f"現在のデータは{data}です")
for dat in data:
    print("f都市別データは{dat}です")
    for d in dat:
        print(d, end="\t")
    print()

print(f"{data[0][0]}の最高気温は{data[0][1]}最低気温は{data[0][2]}です")


# 練習 p136 (10/27)
# 1
score = [74, 85, 69, 77, 81]

print(f"テストの点は{score}です")
print(f"最高点は{max(score)}です")
print(f"最低点は{min(score)}です")
print(f"平均点は{sum(score) / len(score)}です")


# 2
score = [74, 85, 69, 77, 81]

print(f"テストの点は{score}です")
print(f"昇順は{sorted(score)}です")
print(f"降順は{sorted(score, reverse=True)}です")


# 3
score = [74, 85, 69, 77, 81]
print(f"テストの点は{score}です")

nscore = [i for i in score if i >= 80]

print(f"80点以上は{nscore}です")
print(f"80点以上の人は{len(nscore)}です")


# 4
city = ["東京", "名古屋", "大阪", "京都", "福岡"]
maxTemp = [32, 38, 27, 26, 27]
minTemp = [25, 21, 20, 19, 22]

print(f"都市名データは{city}です")
print(f"最高気温データは{maxTemp}です")
print(f"最低気温データは{minTemp}です")

for c, ma, mi in zip(city, maxTemp, minTemp):
    print(f"{c}の最高気温は{ma} 最低気温は{mi}です")
