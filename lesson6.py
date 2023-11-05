### Lesson6 (10/27)

# sample1
sale = {
    "東京":80,
    "名古屋":60,
    "京都":22,
    "大阪":50,
    "福岡":75,   #縦並びの時は最後カンマあったほうが良いかも
}
print(f"現在のデータは{sale}です")

k = input("どの支店のデータを表示しますか？")
print(f"{k}のデータは{sale[k]}です")

# in演算子を使うことでキーが存在することの判定ができる
# sample3
sale = {
    "東京":80,
    "名古屋":60,
    "京都":22,
    "大阪":50,
    "福岡":75,
}
print(f"現在のデータは{sale}です")

k = input("追加するキーを入力>>>")
if k in sale:
    print(f"{k}のデータはすでに存在しています。")
else:
    d = int(input("追加するデータを入力>>>"))
    sale[k] = d
    print(f"{k}のデータとして{sale[k]}を追加しました。")
print(f"現在のデータは{sale}です")

k = input("どのデータを変更しますか？>>>")
if k in sale:
    print(f"{k}のデータは{sale[k]}です。")
    d = int(input("データを入力>>>"))
    sale[k] = d
    print(f"{k}のデータは{sale[k]}に変更されました")
else:
    print(f"{k}のデータは見つかりませんでした")
print(f"現在のデータは{sale}です")

k = input("どのデータを削除しますか？>>>")
if k in sale:
    print(f"{k}のデータは{sale[k]}です。")
    # オリジナル消して良いか再度確認
    ans = input("削除してよろしいですか？(y/n)")
    if ans == "y":
        del sale[k]
        print("データを削除しました")
    else:
        print("削除をキャンセルしました")

else:
    print(f"{k}のデータは見つかりませんでした")
print(f"現在のデータは{sale}です")


# sample4
sale = {
    "東京":80,
    "名古屋":60,
    "京都":22,
    "大阪":50,
    "福岡":75,
}
print(f"現在のデータは{sale}です")

print("キーを表示します")
for k in sale.keys():
    print(k, end="\t")
print()
# ↑何も指定しない場合keyだけ返されるから、あまり使わない

print("値を表示します")
for v in sale.values():
    print(v, end="\t")
print()

print("キーと値を表示します")
for i in sale.items():
    print(i, end="")
print()
# ↑タプルとして返す


# sample5
sale1 = {
    "東京":80,
    "名古屋":60,
    "京都":22,
}
sale2 = {
    "京都":100,
    "大阪":50,
    "福岡":75,
}
print(f"1のデータは{sale1}です")
print(f"2のデータは{sale2}です")
print("1を2で更新します")

sale1.update(sale2)
print(f"1のデータは{sale1}です")