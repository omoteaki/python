### Lesson2 & 3

# 練習
# 1
# 数値を出力する
print(1)
print(3.14)

# 2
# print("123")
print(123)
print("\\", 100, "もらった")
print("またあした")

# 3
print("1\t2\t3\t4\t5\t6")
print(1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6)


# Lesson3ここから
# 変数

age = 10
name = "hoge"
print(f"私の名前は{name}です。年齢は{age}です")

# sample2
sale = 10
print(f"売り上げは{sale}万円です")
print("売り上げの値を変更します")
sale = 20
print(f"売り上げは{sale}万円です")

# sample3
name = "東京"
sale = 10
print(f"{name}支店の売上は{sale}万円です")

# sample4
print("1+2は", 1+2,"です")

# sample5
price = 50
num = 10
total = price * num
print(f"単価は{price}円です。")
print(f"売上個数は{num}個です。")
print(f"合計金額は{total}円です。")

total = total - 100
print(f"値引きすると{total}円です")

# sample6
num1 = 11
num2 = 5
print(f"num1+num2は{num1 + num2}です")
print(f"num1-num2は{num1 - num2}です")
print(f"num1*num2は{num1 * num2}です")
print(f"num1/num2は{num1 / num2}です")
print(f"num1%num2は{num1 % num2}です")

# sample7
num = 10
pic = "○"
graph = pic * num

# print()へのわたし方色々
# 連結して一つの文字列をprintにわたしている
print("売上：" + graph)
# 最初から一つの文字列
print(f"売上：{graph}")
# 二つの値をprint()にわたしている
print(num,"万円の売上があります")


# sample8
n = input("値を入力してください")
print(n, "が入力されました")

# sample9
num1 = int(input("整数1を入力してください"))
num2 = int(input("整数2を入力してください"))
num3 = num1 + num2
print(f"{num1}+{num2}は{num3}です")

# 練習
# 1
age = input("あなたは何才ですか？")
print("あなたは" + age + "才です")

# 2
tall = float(input("身長を入力してください"))
weight = float(input("体重を入力してください"))
print("身長は" , tall, "センチです")
print("体重は", weight, "キロです")
