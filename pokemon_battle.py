import random


print("＝＝ポケモンバトル＝＝")
player = "ピカチュウ"
enemy = "ヒトカゲ"
player_hp = 50
enemy_hp = 50
print(f"野生の{enemy}が現れた！")
print(f"{player}　HP:{player_hp}")
print(f"{enemy}　HP:{enemy_hp}")
print(f"どうする？")
print(f"1こうげき")
print(f"2逃げる")

while True:
    sentaku = input("1か2を入力してください:")
    if sentaku == "1":
        print(f"{player}のこうげき")
        print("こうげきした！")

        random_number = random.randint(5, 10)
        enemy_hp -= random_number
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy}のHPは{enemy_hp}になった")

        if enemy_hp <= 0:
            print("相手のHPが0になった")
            print("勝利！！")
            break

        random_number = random.randint(5, 10)
        player_hp -= random_number
        if player_hp < 0:
                player_hp = 0
        print(f"{enemy}のこうげき")
        print(f"{player}のHPは{player_hp}になった")

        if player_hp <= 0:
            print("HPが0になった！")
            print("目の前が真っ暗になった！")
            break

    elif sentaku == "2":
        random_number2 = random.random()

        if random_number2 < 0.1:
            input("にげきれた！")
            break
        else:
            input("にげきれなかった")
            random_number = random.randint(5, 10)
            player_hp -= random_number
            if player_hp < 0:
                player_hp = 0
            print(f"{enemy}のこうげき")
            print(f"{player}のHPは{player_hp}になった")

            if player_hp <= 0:
                print("HPが0になった！")
                print("目の前が真っ暗になった！")
                break
