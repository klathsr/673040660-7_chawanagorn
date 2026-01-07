"""
Chawanagorn Thiangsiri
673040660-7
Lab4-2 P3
"""

from datetime import datetime

class VideoGame:

    total_players = 0
    difficulty_levels = ["Easy", "Medium", "Hard"]
    max_level = 100
    server_start_time = datetime.now()
    active_players = []
    leaderboard = {}

 
    def __init__(self, player_name, character_type):
        if not VideoGame.is_valid_character_name(player_name):
            raise ValueError("Invalid character name")

        self.player_name = player_name
        self.character_type = character_type
        self.level = 1
        self.health = 100
        self.exp = 0
        self.coins = 0
        self.inventory = []
        self.is_alive = True

        VideoGame.total_players += 1
        VideoGame.active_players.append(player_name)
        VideoGame.leaderboard[player_name] = 0


    def level_up(self):
        self.level += 1
        self.health = 100
        VideoGame.leaderboard[self.player_name] = self.level * 100 + self.coins
        print(f"{self.player_name} leveled up to {self.level}")

    def collect_coins(self, amount):
        self.coins += amount
        VideoGame.leaderboard[self.player_name] = self.level * 100 + self.coins
        print(f"{self.player_name} coins: {self.coins}")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
            VideoGame.active_players.remove(self.player_name)
            print(f"{self.player_name} has died.")
        else:
            print(f"{self.player_name} health: {self.health}")

    def fight_monster(self, monster_name, monster_level):
        damage = VideoGame.calculate_damage(10, 5, monster_level)
        self.take_damage(damage)

        if self.is_alive:
            self.exp += 10 * monster_level
            self.collect_coins(3 * monster_level)

            if self.exp >= VideoGame.calculate_exp_needed(self.level):
                self.exp = 0
                self.level_up()

        print(f"Fought {monster_name} (Lv.{monster_level})")

    def get_stats(self):
        return (
            f"{self.player_name} | Lv:{self.level} | HP:{self.health} | "
            f"Coins:{self.coins} | Alive:{self.is_alive}"
        )

    @classmethod
    def create_party(cls, players, player_type):
        return [cls(name, player_type) for name in players]

    @classmethod
    def get_server_stats(cls):
        uptime = datetime.now() - cls.server_start_time
        return (
            f"Players: {cls.total_players}\n"
            f"Active: {cls.active_players}\n"
            f"Leaderboard: {cls.leaderboard}\n"
            f"Uptime: {uptime}"
        )

    @classmethod
    def get_leaderboard(cls):
        sorted_lb = sorted(cls.leaderboard.items(), key=lambda x: x[1], reverse=True)
        return sorted_lb

    @classmethod
    def reset_server(cls):
        cls.total_players = 0
        cls.active_players.clear()
        cls.leaderboard.clear()
        cls.server_start_time = datetime.now()

    @staticmethod
    def calculate_damage(attack, defense, level):
        return max(0, (attack * level) - defense)

    @staticmethod
    def calculate_exp_needed(level):
        return 100 * level

    @staticmethod
    def is_valid_character_name(name):
        return name.isalnum() and 3 <= len(name) <= 20

    @staticmethod
    def get_rank_title(level):
        if level < 20:
            return "Beginner"
        elif level < 50:
            return "Warrior"
        elif level < 80:
            return "Elite"
        else:
            return "Legend"
