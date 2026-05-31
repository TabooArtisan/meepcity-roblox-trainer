"""Unit tests for MeepCity trainer core."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core import MeepCityTrainer


class TestMeepCityTrainer:
    """Test suite for MeepCityTrainer."""

    def setup_method(self):
        self.trainer = MeepCityTrainer("test_user")

    def test_initial_stats(self):
        stats = self.trainer.get_stats()
        assert stats["username"] == "test_user"
        assert stats["coins"] == 0
        assert stats["xp"] == 0
        assert stats["running"] == False

    def test_collect_coins_positive(self):
        result = self.trainer.collect_coins()
        assert result > 0
        assert self.trainer.coins > 0

    def test_earn_xp_default(self):
        result = self.trainer.earn_xp(tasks=1)
        assert result >= 10
        assert self.trainer.xp >= 10

    def test_start_stop(self):
        self.trainer.start_auto_farm(cycles=2)
        assert self.trainer.coins > 0
        assert self.trainer.xp > 0
        assert self.trainer.is_running == False

    def test_stop_while_running(self):
        self.trainer.is_running = True
        self.trainer.stop()
        assert self.trainer.is_running == False