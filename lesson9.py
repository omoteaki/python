### Lesson9 文字列と正規表現

# sample1
str = input("文字列を入力してください")

print(f"文字列は、{str} です")
print(f"0番目の文字は、{str[0]} です")
print(f"文字列を逆順にすると、{str[::-1]} です")
print(f"文字列の長さは、{len(str)} です")

# sample2
str = input("文字列を入力してください")

print(f"文字列は、{str} です")
print(f"大文字にすると、{str.upper()} です")
print(f"大文字にすると、{str.lower()} です")

# sample3
word0 = input("1つ目の単語を入力してください。")
word1 = input("2つ目の単語を入力してください。")
word2 = input("3つ目の単語を入力してください。")

print("{0}は{1}{2}です。{2}です。".format(word0, word1, word2))

num0 = int(input("個数を入力して下さい。"))
num1 = int(input("金額を入力して下さい。"))

print("{0:<}個{1:>10,}円".format(num0, num1))
# {>10,}右揃えで、10桁のカンマ区切り表示

# sample4
str = input("文字列を入力してください")
key = input("検索する文字列を入力してください")

res = str.find(key)

if res != -1:
    print(f"{str}の{res}の位置に{key}が見つかりました")
else:
    print(f"{str}の中に{key}が見つかりませんでした")

# 位置は知らなくて良い場合
if key in str:
    print(f"{str}の中に{key}が見つかりました")
else:
    print(f"{str}の中に{key}が見つかりませんでした")


# sample5
str1 = input("文字列を入力してください")
old = input("置換される文字列を入力してください")
new = input("置換する文字列を入力してください")

if old in str1:
    str2 = str1.replace(old, new)
    print(f"{str2}に置換しました")
else:
    print(f"{str1}の中に{old}が見つかりませんでした")


# 正規表現
# sample6
import re

# ptr = ["Apple", "GoodBye", "Thankyou"]   # パターン文字列
ptr = ["lo", "o", "yo"]   # パターン文字列
str = ["Hello", "GoodBye", "Thankyou"]   # 検索対象文字列

for valueptr in ptr:
    print("------")
    pattern = re.compile(valueptr)   # パターン文字列をコンパイル
    for valuestr in str:
        res = pattern.search(valuestr)   # 戻り値はNone
        if res is not None:
            m = "◯"
        else:
            m = "×"
        msg = "パターン" + valueptr + "(文字列)" + valuestr + "(マッチ)" + m
        print(msg)

# 上記の出力
'''
------
パターンlo(文字列)Hello(マッチ)◯
パターンlo(文字列)GoodBye(マッチ)×
パターンlo(文字列)Thankyou(マッチ)×
------
パターンo(文字列)Hello(マッチ)◯
パターンo(文字列)GoodBye(マッチ)◯
パターンo(文字列)Thankyou(マッチ)◯
------
パターンyo(文字列)Hello(マッチ)×
パターンyo(文字列)GoodBye(マッチ)×
パターンyo(文字列)Thankyou(マッチ)◯
'''

# メタ文字を使ったパターン
# sample7
import re

# パターン文字列
ptr = [
    "TXT",
    "^TXT",
    "TXT$",
    "^TXT$",
]
# 検索対象文字列
str = [
    "TXT",
    "TXTT",
    "TXTTT",
    "TTXT",
]

for valueptr in ptr:
    print("------")
    pattern = re.compile(valueptr)   # パターン文字列をコンパイル
    for valuestr in str:
        res = pattern.search(valuestr)   # 戻り値はNone
        if res is not None:
            m = "◯"
        else:
            m = "×"
        msg = "パターン" + valueptr + "(文字列)" + valuestr + "(マッチ)" + m
        print(msg)