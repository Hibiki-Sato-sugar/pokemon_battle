import random


class Pokemon:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp

    def take_damage(self, damage: int) -> int:
        actual_damage = min(damage, self.current_hp)
        self.current_hp -= actual_damage
        return actual_damage

    def is_fainted(self) -> bool:
        return self.current_hp <= 0


def display_hp(player: Pokemon, enemy: Pokemon) -> None:
    print(f"{player.name} HP {player.current_hp}")
    print(f"{enemy.name} HP {enemy.current_hp}")
    print()


def player_attack(enemy: Pokemon) -> None:
    damage = random.randint(5, 10)
    actual_damage = enemy.take_damage(damage)
    print(f"ピカチュウのこうげき！ {enemy.name}に {actual_damage} のダメージ！")


def player_run() -> bool:
    if random.random() < 0.1:
        print("逃げ切れた！")
        return True
    print("逃げられなかった！")
    return False


def enemy_attack(player: Pokemon, enemy: Pokemon) -> None:
    damage = random.randint(5, 10)
    actual_damage = player.take_damage(damage)
    print(f"{enemy.name}のこうげき！ {player.name}に {actual_damage} のダメージ！")


def get_player_command() -> str:
    while True:
        command = input("こうげき / にげる > ").strip()
        if command in ("こうげき", "にげる"):
            return command
        print("「こうげき」か「にげる」を入力してください。")


def battle(player: Pokemon, enemy: Pokemon) -> None:
    print("=== ポケモンバトル ===")
    print()

    while True:
        display_hp(player, enemy)

        command = get_player_command()

        if command == "こうげき":
            player_attack(enemy)
            if enemy.is_fainted():
                display_hp(player, enemy)
                print("勝利！")
                return

            enemy_attack(player, enemy)
            if player.is_fainted() and enemy.is_fainted():
                display_hp(player, enemy)
                print("目の前が真っ暗になった")
                return
            if player.is_fainted():
                display_hp(player, enemy)
                print("目の前が真っ暗になった")
                return

        elif command == "にげる":
            if player_run():
                return

            enemy_attack(player, enemy)
            if player.is_fainted():
                display_hp(player, enemy)
                print("目の前が真っ暗になった")
                return


def main() -> None:
    player = Pokemon("ピカチュウ", 50)
    enemy = Pokemon("ヒトカゲ", 50)
    battle(player, enemy)


if __name__ == "__main__":
    main()
