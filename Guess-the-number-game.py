import random

n, m = map(int, input("二つの数字をスペースで区切り、昇順で入力してください").split())

if n > m:
    n, m = m, n

random_num = random.randint(n, m)

for i in range(n):
    guess_num = int(input("乱数で選ばれた数字を予想し、入力してください"))
    if random_num == guess_num:
        print("あたり")
        exit()
    else:
        print("はずれ")