# まず、ランダムな数字を生成するためにrandomモジュールを読み込みます。
import random

# 1から100までの間で、コンピュータがランダムな数字を1つ選びます。
answer = random.randint(1, 100)

# プレイヤーの予想回数を数えるための変数を用意します。
guesses = 0

print("数当てゲームへようこそ！")
print("1から100までの数字を当ててね。")

# プレイヤーが正解するまで、繰り返し処理を行います。
while True:
    # プレイヤーから数字を入力してもらいます。
    # input()で受け取る値は「文字列」なので、int()で「整数」に変換します。
    user_guess = int(input("予想を入力してください: "))
    
    # 予想回数を1つ増やします。
    guesses = guesses + 1
    
    # プレイヤーの予想と答えを比較します。
    if user_guess < answer:
        print("もっと大きいよ。")
    elif user_guess > answer:
        print("もっと小さいよ。")
    else:
        # 正解した場合の処理
        print(f"正解！おめでとう！")
        print(f"{guesses}回で当てました。")
        # 正解したので、ループを終了します。
        break
