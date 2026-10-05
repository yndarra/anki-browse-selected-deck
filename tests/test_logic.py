"""Тесты решения «переключать ли браузер». Запуск: run_tests.bat."""

from __future__ import annotations

import os
import sys
import unittest

# Импортируем logic.py напрямую, минуя __init__.py (тот требует GUI Anki).
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "src", "browse_selected_deck")
)
from logic import should_switch  # noqa: E402


class ShouldSwitchTest(unittest.TestCase):
    def test_changed_mode_switches_only_on_new_deck(self) -> None:
        self.assertTrue(should_switch("changed", 1, 2, False, False))
        self.assertFalse(should_switch("changed", 2, 2, False, False))

    def test_unknown_last_deck_switches(self) -> None:
        self.assertTrue(should_switch("changed", None, 2, False, False))

    def test_always_mode(self) -> None:
        self.assertTrue(should_switch("always", 2, 2, False, False))

    def test_anki_handles_card_and_search_itself(self) -> None:
        # Из повторения (карточка) или с готовым поиском — не вмешиваемся.
        for mode in ("changed", "always"):
            self.assertFalse(should_switch(mode, 1, 2, True, False))
            self.assertFalse(should_switch(mode, 1, 2, False, True))


if __name__ == "__main__":
    unittest.main()
