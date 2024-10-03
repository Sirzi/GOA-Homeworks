score = int(input("Player score: "))
is_passing = score > 50
is_high_passing = score > 75 and score < 99
is_perfect = score == 100
is_failing = score < 50
print("Player is passing: ", is_passing)
print("Player is passing with high points: ", is_high_passing)
print("Player got perfect score: ", is_perfect)
print("Player failed: ", is_failing)

