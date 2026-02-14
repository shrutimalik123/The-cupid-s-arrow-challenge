import random

def cupids_arrow():
    # 1. Game Setup
    target_pos = random.randint(40, 60) # Target is between 40m and 60m
    wind = random.randint(-5, 5) # Positive = East, Negative = West
    arrows = 3
    won = False

    print("--- 💘 CUPID'S ARROW CHALLENGE 💘 ---")
    print(f"Target Distance: {target_pos}m")
    print(f"Current Wind Speed: {wind}m/s")
    print("Goal: Hit the target exactly. Your arrow flies: (Power + Wind)")

    # 2. Game Loop
    while arrows > 0 and not won:
        print(f"\n🏹 Arrows left: {arrows}")
        
        try:
            power = int(input("Enter Shot Power (1-100): "))
        except ValueError:
            print("❌ Please enter a number!")
            continue

        # 3. Physics Logic
        # Total distance = the player's power adjusted by the wind
        result = power + wind
        distance_diff = result - target_pos

        if result == target_pos:
            print(f"🎯 BULLSEYE! The arrow landed at {result}m. Love is in the air!")
            won = True
        elif abs(distance_diff) <= 3:
            print(f"💖 SO CLOSE! You landed at {result}m. Just missed the heart!")
        elif result < target_pos:
            print(f"📉 TOO SHORT! The arrow landed at {result}m.")
        else:
            print(f"📈 TOO LONG! The arrow flew past to {result}m.")

        arrows -= 1

    # 4. End State
    if won:
        print("\n🏆 Happy Valentine's Day! You've successfully spread the love.")
    else:
        print(f"\n🥀 Out of arrows! The target was at {target_pos}m. Better luck next year!")

cupids_arrow()
