"""Core trainer logic for MeepCity auto-farming."""

import time
import random
import logging
from colorama import Fore, Style, init

init(autoreset=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MeepCityTrainer:
    """Handles MeepCity automation tasks."""

    def __init__(self, username: str = "player1"):
        self.username = username
        self.coins = 0
        self.xp = 0
        self.is_running = False

    def _simulate_action(self, action_name: str, duration: float = 1.0) -> bool:
        """Simulate a game action with random delay."""
        delay = random.uniform(0.5, 2.0)
        logger.info(f"{Fore.CYAN}[{self.username}] {action_name}... waiting {delay:.1f}s")
        time.sleep(delay)
        return True

    def collect_coins(self, amount: int = 50) -> int:
        """Simulate coin collection."""
        if not self._simulate_action("Collecting coins"):
            return 0
        collected = random.randint(5, 15)
        self.coins += collected
        logger.info(f"{Fore.GREEN}+{collected} coins (total: {self.coins})")
        return collected

    def earn_xp(self, tasks: int = 3) -> int:
        """Simulate XP earning by completing tasks."""
        total_xp = 0
        for i in range(tasks):
            if not self._simulate_action(f"Task {i+1}/{tasks}"):
                continue
            xp_gain = random.randint(10, 30)
            self.xp += xp_gain
            total_xp += xp_gain
            logger.info(f"{Fore.YELLOW}+{xp_gain} XP (total: {self.xp})")
        return total_xp

    def start_auto_farm(self, cycles: int = 5):
        """Run automated farming loop."""
        self.is_running = True
        logger.info(f"{Fore.MAGENTA}Starting auto-farm for {cycles} cycles")
        for cycle in range(1, cycles + 1):
            if not self.is_running:
                break
            logger.info(f"{Fore.BLUE}--- Cycle {cycle}/{cycles} ---")
            self.collect_coins()
            self.earn_xp(tasks=random.randint(1, 3))
            time.sleep(random.uniform(1.0, 3.0))
        self.is_running = False
        logger.info(f"{Fore.GREEN}Auto-farm complete. Coins: {self.coins}, XP: {self.xp}")

    def stop(self):
        """Stop the trainer."""
        self.is_running = False
        logger.info(f"{Fore.RED}Trainer stopped.")

    def get_stats(self) -> dict:
        """Return current stats."""
        return {
            "username": self.username,
            "coins": self.coins,
            "xp": self.xp,
            "running": self.is_running
        }