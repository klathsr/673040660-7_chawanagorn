from P3f import VideoGame

p1 = VideoGame("Hero01", "Ninja")
p2 = VideoGame("Mage99", "Wizard")

p1.fight_monster("Slime", 2)
p2.collect_coins(50)

print(p1.get_stats())
print(VideoGame.get_leaderboard())
print(VideoGame.get_server_stats())
