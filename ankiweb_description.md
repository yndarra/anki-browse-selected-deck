<b>Browse (or B) switches an already open browser to the deck selected on the main screen.</b>

In Anki, Shift+click on a deck row selects that deck. <i>Add</i> then opens the Add window for that deck, even if the window is already open. <i>Browse</i>, however, only opens on that deck if the browser was closed. If it is already open, it just comes to the front with the old search.

This add-on makes <i>Browse</i> work like <i>Add</i>:
<ul>
<li><b>changed</b> mode (default): the open browser switches to the selected deck if a different deck was selected since last time. Otherwise your current search is kept.</li>
<li><b>always</b> mode: every Browse returns the browser to the selected deck.</li>
<li>It uses the same search Anki uses when opening the browser from scratch (<code>deck:current</code> or your "Default search text").</li>
<li>During review, Browse behaves as in Anki and shows the current card.</li>
<li>Only the main browser window is affected. Extra windows from <a href="https://ankiweb.net/shared/info/1978418160">Multiple Browser Windows</a> keep their searches.</li>
</ul>

Settings: Tools → Add-ons → Config → <code>"mode": "changed"</code> / <code>"always"</code>.

Source code: <a href="https://github.com/yndarra/anki-browse-selected-deck">github.com/yndarra/anki-browse-selected-deck</a>

<i>RU: «Обзор» переключает уже открытый браузер на колоду, выбранную на главном экране (Shift+клик).</i>
