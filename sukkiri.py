# 参考書、スッキリわかるPython入門より
# 組み込み関数・ライブラリの練習問題

# 7-2 関数の呼び出し方の違い
'''
import A 
A.func()

import A as B
B.func()
'''

# 7-3 関数だけ読み込む
'''
from A import func
'''


# 7-4
# '''
num1 = int(input("一つ目の数値を入力してください"))
num2 = int(input("二つ目の数値を入力してください"))
num3 = int(input("三つ目の数値を入力してください"))

list = [num1, num2, num3]

print(max(list))
# '''

# 解答
# '''
nums = list()
for n in range(3):
    # data = int(input("{}個目の整数を入力してください>>>".format(n + 1)))
    data = int(input(f"{n + 1}個目の整数を入力してください>>>"))   #f-string
    nums.append(data)
print(max(nums))
# '''

# 7−4
'''
pi = 3.141592
for i in range(0,6):
    print(f"小数点以下第{i}位を四捨五入すると{round(pi, i)}")
'''


# 7-5
file = open("sample.txt", 'r')
file2 = open("sample2.txt", 'a')
for line in file:
    # print(line)
    # file2.write(line + "\n")
    file2.write(line)
file.close()
file2.close()

# 7-6
'''
from random import randint
print("数当てゲームを始めます。3桁の数を当ててください!")

while True:
    # answer = list()

    answer = [1,2,3]
    prediction = list()
    for n in range(3):
        answer.append(randint(0,9))

    for i in range(3):
        prediction.append(int(input(f"{i + 1}桁目の予想を入力(0~9)>>>")))

    print(prediction, answer)

    hit = 0
    ball = 0
    for c in range(3):
        if answer[c] == prediction[c]:
            hit += 1
        else:
            ball += 1

    print(f"{hit}ヒット！{ball}ボール！")
    if hit == 3:
        print("正解です！")

    num = int(input("続けますか？1:続ける 2:終了>>"))
    if num == 2:
        break

print(f"正解は{answer[0] * 100 + answer[1] * 10 + answer[2]}")
'''
# ボールの解釈を間違えていた

#解答
from random import randint
print("数当てゲームを始めます。3桁の数を当ててください！")

# 正解を作成
answer = list()
for n in range(3):
    answer.append(randint(0,9))
print(answer)

is_continue = True
while is_continue == True:
    # 予想の入力
    prediction = list()
    for n in range(3):
        data = int(input(f"{n + 1}桁目の予想入力(0~9)>>"))
        prediction.append(data)

    # 答え合わせ
    hit = 0
    blow = 0
    for n in range(3):
        if prediction[n] == answer[n]:
            hit += 1
        else:
            for m in range(3):
                if prediction[n] == answer[m]:
                    blow += 1
                    break

    # 結果発表
    print(f"{hit}ヒット！{blow}ボール！")
    if hit == 3:
        print("正解です！")
        is_continue = False
    else:
        if int(input("続けますか？ 1:続ける 2:終了>>")) == 2:
            print(f"正解は{answer[0]}{answer[1]}{answer[2]}でした")
            is_continue = False