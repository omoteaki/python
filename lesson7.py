### Lesson7-関数

# sample2
def sell():
    print("販売が行われました")

sell()

print("もう一度販売を行います")
sell()


# sample3
def sell(place):
    print(f"{place} 支店の販売が行われました")

sell("東京")
sell("大阪")


# 複数の引数を持つ関数
# sample5
def sell(place, num):
    print(f"{place} 支店で{num}万円の販売が行われました")

sell("東京", 5)


# デフォルト引数を定義すれば
def sum(num1, num2=0):
    return num1 + num2
# 引数の数が等しくなくてもエラーは出ない
ans = sum(5)


# 戻り値
# sample6
def sell(place, price, num):
    print(f"{place}支店で{num}社に{price}万円の販売が行われました")
    tt = price * num
    return tt
    return 100   # return の後の文は処理されない

total = sell("東京", 100, 5)
print(f"売上は{total}万円でした")

# ちなみに
# return a,b
# ↑はタプルとして返しちゃう return (a, b)


# (10/31)
# 関数をリストに代入する
# sample8
def append():
    print("データを追加します")

def update():
    print("データを変更します")

def delete():
    print("データを削除します")

list = [append, update, delete]

res = int(input("操作番号を入力してください。(0~2)"))

if 0 <= res and res < len(list):
    list[res]()   # 関数を呼び出すことができる


# sample9
data = [1, 2, 3, 4, 5]
for d in map(lambda x: x*2, data):
    print(d)

# map(関数, イテラブル) 戻り値はイテレータ


# 変数のスコープ
# sample11
a = 0

def funcB():
    b = 1
    print("funcBのなかで変数aと変数bが使えます。")
    print(f"変数aの値は{a}です")
    print(f"変数aの値は{b}です")
    # print(f"変数aの値は{c}です")

def funcC():
    c = 2
    print("funcCのなかで変数aと変数cが使えます。")
    print(f"変数aの値は{a}です")
    # print(f"変数aの値は{b}です")
    print(f"変数aの値は{c}です")

print("関数の外で変数aが使えます")
print(f"変数aの値は{a}です")
# print(f"変数aの値は{b}です")
# print(f"変数aの値は{c}です")

funcB()
funcC()


# 練習
# 1
def rpast(num):
    # print("*" * num, end="") # 最後の改行はいらない
    print("*" * num)

num = int(input("個数を入力してください"))
rpast(num)


# 2
# def rpstr(num, str="*"):
#   if(str == ""):
#     str = "*"
#   print(str * num, end="")

# str = input("文字列を入力してください")
# num = int(input("個数を入力してください"))
# rpstr(num,str)

# 2の答え
def rpstr(num, str="*"):
    print(str * num)

str = input("文字列を入力してください")
num = int(input("個数を入力してください"))

print("文字列あり---")
rpstr(num, str)
print("文字列なし---")
rpstr(num)
