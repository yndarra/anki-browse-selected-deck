"""Browse Selected Deck — «Обзор» переключает уже открытый браузер на выбранную колоду.

Как устроено в самой Anki:
  • Shift+клик по строке колоды на главном экране делает её текущей.
  • Если браузер закрыт, «Обзор» (или клавиша B) открывает его с поиском по
    умолчанию — обычно `deck:current`, то есть сразу на текущей колоде.
  • Если браузер УЖЕ открыт, Anki вызывает Browser.reopen() без карточки и без
    поиска, и тот ничего не делает: окно просто выходит вперёд со старым поиском.

Дополнение оборачивает Browser.reopen(): в этом случае, если выбрана другая
колода (или в режиме "always" — всегда), браузер заново выполняет поиск по
умолчанию, то есть переходит к выбранной колоде.

Затрагивается только ОСНОВНОЕ окно браузера (диалог "Browser" в aqt.dialogs).
Дополнительные окна из Multiple Browser Windows живут под своими именами
и не меняются.
"""

from __future__ import annotations

from typing import Any

import aqt
from anki.collection import SearchNode
from aqt import gui_hooks, mw
from aqt.browser import Browser

from .logic import MODES, should_switch

ADDON = __name__.split(".")[0]


def _mode() -> str:
    cfg = mw.addonManager.getConfig(ADDON) or {}
    mode = cfg.get("mode", "changed")
    return mode if mode in MODES else "changed"


def _is_main_browser(browser: Browser) -> bool:
    """Это основное окно браузера, а не дополнительное (Multiple Browser Windows)?"""
    entry = aqt.dialogs._dialogs.get("Browser")
    return bool(entry) and entry[1] is browser


def _remember_deck(browser: Browser) -> None:
    """Запоминаем, на какой колоде браузер сейчас «стоит» с нашей точки зрения."""
    browser._bsd_deck = mw.col.decks.get_current_id()  # type: ignore[attr-defined]


def _search_selected_deck(browser: Browser) -> None:
    """Поиск по умолчанию — тот же, с которым Anki открывает браузер с нуля.

    Обычно это `deck:current`. Если в настройках Anki (Обзор → поиск по
    умолчанию) задан свой текст, используется он — как при первом открытии.
    """
    default_search = getattr(browser, "_default_search", None)
    if callable(default_search):
        default_search()
    else:
        browser.search_for_terms(SearchNode(deck="current"))


_original_reopen = Browser.reopen


def _reopen(self: Browser, _mw: Any, card: Any = None, search: Any = None) -> None:
    switch = _is_main_browser(self) and should_switch(
        mode=_mode(),
        last_deck_id=getattr(self, "_bsd_deck", None),
        current_deck_id=mw.col.decks.get_current_id(),
        has_card=card is not None,
        has_search=search is not None,
    )
    _original_reopen(self, _mw, card=card, search=search)
    if not switch:
        if card is not None or search is not None:
            _remember_deck(self)
        return

    def run() -> None:
        _search_selected_deck(self)
        _remember_deck(self)

    # Сначала сохраняем заметку, открытую в редакторе браузера: поиск
    # перезагружает список, и несохранённая правка иначе могла бы потеряться.
    editor = getattr(self, "editor", None)
    if editor is not None:
        editor.call_after_note_saved(run)
    else:
        run()


Browser.reopen = _reopen  # type: ignore[method-assign]


def _on_browser_will_show(browser: Browser) -> None:
    # Браузер открылся с нуля — уже на текущей колоде.
    _remember_deck(browser)


gui_hooks.browser_will_show.append(_on_browser_will_show)
