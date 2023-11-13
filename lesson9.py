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


# sample8
import re

ptr = [
    "TXT.",
    "TXT..",
    ".TXT",
    "..TXT",
]
str = [
    "TXT",
    "TXTT",
    "TXTTT",
    "TTXT",
    "TTTXT",
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


# sample9
import re

ptr = [
    "[012]",   # 3だけx
    "[0-3]",   # 全部o
    "[^012]",   # 3だけo
]
str = ["0", "1", "2", "3"]

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


# 繰り返しの正規表現
# sample10
import re

ptr = [
    "T*",   # 0回以上の繰り返し (全部o)
    "T+",   # 1回以上の繰り返し (X以外o)
    "T?",   # 0または1回の繰り返し (Xだけo だと思っていたけど、実行結果は全部o。0回の繰り返しだからTがなくてもマッチする)
    "T{3}",   # 3回の繰り返し (TTTだけo だと思っていたけど、実行結果はTTTTもo。3回の繰り返しを含んでいるからマッチする)
]
str = [
    "X",
    "TT",
    "TTT",
    "TTTT",
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


# グループ化と選択を行う正規表現
# sample11
import re

ptr = [
    "(TXT)+",   # TXTとTXTXTがo
    "TXT|XTX",   # TX以外o
]
str = [
    "TX",
    "TXT",
    "XTX",
    "TXTXT",
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


# sample12
import re

ptr = "\.(csv|html|py)$"
str = [
    "sample.csv",
    "sample.exe",
    "test.py",
    "index.html",
]

pattern = re.compile(ptr)
for valuestr in str:
    res = pattern.sub(".txt", valuestr)
    msg = "(変換前)" + valuestr + "(変換後)" + res
    print(msg)