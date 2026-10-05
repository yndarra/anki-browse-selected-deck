"""Решение «переключать ли уже открытый браузер на выбранную колоду».

Чистая функция без Anki — её проверяют тесты (tests/test_logic.py).
"""

from __future__ import annotations

# Режимы из config.json:
#   "changed" — переключать, только если с прошлого раза выбрана ДРУГАЯ колода
#               (иначе твой текущий поиск в браузере не сбрасывается);
#   "always"  — каждое нажатие «Обзор» возвращает браузер к выбранной колоде.
MODES = ("changed", "always")


def should_switch(
    mode: str,
    last_deck_id: int | None,
    current_deck_id: int,
    has_card: bool,
    has_search: bool,
) -> bool:
    """Нужно ли заново выполнить поиск по выбранной колоде.

    has_card / has_search — что Anki сама передала при открытии браузера:
    из режима повторения приходит карточка, из других мест — готовый поиск.
    В обоих случаях Anki всё делает сама, и мы не вмешиваемся.
    """
    if has_card or has_search:
        return False
    if mode == "always":
        return True
    return last_deck_id != current_deck_id
