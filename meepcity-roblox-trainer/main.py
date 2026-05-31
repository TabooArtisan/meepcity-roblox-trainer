"""Entry point for MeepCity Roblox Trainer."""

import sys
import time
from src.core import MeepCityTrainer
from src.utils import save_profile, load_profile


def main():
    print("=" * 50)
    print("   MeepCity Roblox Trainer v1.0")
    print("=" * 50)

    profile = load_profile()
    username = profile.get("username", input("Enter your username: ") or "player1")
    trainer = MeepCityTrainer(username)

    while True:
        print("\nOptions:")
        print("1. Start auto-farm (5 cycles)")
        print("2. Collect coins once")
        print("3. Earn XP once")
        print("4. Show stats")
        print("5. Save & Exit")

        choice = input("Select: ").strip()

        if choice == "1":
            trainer.start_auto_farm(cycles=5)
        elif choice == "2":
            trainer.collect_coins()
        elif choice == "3":
            trainer.earn_xp()
        elif choice == "4":
            stats = trainer.get_stats()
            print(f"Username: {stats['username']}")
            print(f"Coins: {stats['coins']}")
            print(f"XP: {stats['xp']}")
            print(f"Running: {stats['running']}")
        elif choice == "5":
            save_profile(trainer.get_stats())
            print("Profile saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

        time.sleep(0.5)


if __name__ == "__main__":
    main()