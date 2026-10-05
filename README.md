# Browse Selected Deck

A small Anki add-on: **Browse** (or the `B` key) switches an **already open** browser to the deck selected on the main screen.

In Anki, `Shift`+click on a deck row in the deck list selects that deck without opening it. Then:
- **Add** opens the Add window for that deck, even if the window is already open;
- **Browse** opens the browser on that deck **only if the browser was closed**. If it is already open, Anki just brings it to the front with the old search.

This add-on makes **Browse** behave like **Add**: if a different deck is selected, the open browser switches to it.

## Behaviour
- The browser runs the same search Anki uses when it opens the browser from scratch. By default that is `deck:current`, or your *Default search text* if you set one in Preferences → Browsing.
- **`changed` mode** (default): the browser switches only if a different deck was selected since last time. If you press Browse again with the same deck, your current search is kept.
- **`always` mode**: every Browse click returns the browser to the selected deck.
- During review, Browse behaves as in Anki: the browser opens on the current card.
- Unsaved edits in the browser's editor are saved before switching.
- Only the **main** browser window is affected. Extra windows from [Multiple Browser Windows](https://ankiweb.net/shared/info/1978418160) keep their searches.

## Settings
Tools → Add-ons → *Browse Selected Deck* → Config → `"mode": "changed"` or `"always"`.

## Development
`run_tests.bat` runs the tests, `build.bat` builds `dist/browse_selected_deck.ankiaddon`. Requires Anki 23.10+. Tested with 26.09.

---

# Обзор выбранной колоды (RU)

Shift+клик по строке колоды на главном экране выбирает колоду. «Добавить» и так открывает добавление в неё, даже если окно уже открыто. Это дополнение делает так же с **«Обзор»**: уже открытый браузер переключается на выбранную колоду.

- Режим **`changed`** (по умолчанию): браузер переключается, только если с прошлого раза выбрана **другая** колода. Иначе твой текущий поиск остаётся.
- Режим **`always`**: каждое «Обзор» возвращает браузер к выбранной колоде.
- Во время повторения всё как в Anki: браузер открывается на текущей карточке.
- Меняется только **основное** окно браузера. Дополнительные окна из Multiple Browser Windows не трогаются.

## License
MIT
