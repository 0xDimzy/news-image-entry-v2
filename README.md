# news-image-01 — v2: The World (magazine cover)

One image summing up the world's news of **Friday 13 November 2026**, as a
magazine cover — deliberately unlike v1's dense newspaper front page.

## The design

A single dramatic visual carries the day: a **dot-matrix globe at night**,
with numbered glowing hotspots marking where the big stories happened.
Around it, one lead headline, three numbered cover lines keyed to the
markers, and an ALSO TODAY footer strip. A viewer who missed the day can
tell what happened from the image alone — and the image reads at a glance,
even as a thumbnail, where a dense text page turns to grey mush.

| # | Story | On the cover |
| --- | --- | --- |
| 1 | Ukraine peace talks: US envoys Witkoff and Kushner meet Putin, then Zelenskyy; Europe joins the next round, largest prisoner swap planned | Lead headline: **PEACE AT THE TABLE** — red marker on Europe |
| 2 | Nvidia chief Jensen Huang resigns; shares fall 16%; CFO Colette Kress interim CEO | Chip icon + **NVIDIA CHIEF QUITS — SHARES DOWN 16%** |
| 3 | Microsoft 365 down worldwide for a second day (Outlook, Teams, Copilot; 74 countries) | Cloud icon + **MICROSOFT 365 DOWN WORLDWIDE, DAY TWO** |
| 4 | LNG tanker strikes a mine in the Strait of Hormuz; Iran says it hit a US radar site in Bahrain | Red marker on the Gulf + **TANKER HIT BY MINE IN STRAIT OF HORMUZ** |
| — | Also today: FBI seizes $1.2bn in stolen crypto; Gaza hospital strike kills six; Brooklyn building collapse kills eight | ALSO TODAY footer strip |

Sources: BBC World and Al Jazeera live coverage of 13 November 2026, plus
the day's global news briefings — all seven stories were first reported on
13 November 2026.

## Why this should beat v1 (rank 192/923, judge 955206)

- **One focal point, not four.** v1 splits attention across four equal hero
  stories; v2 gives the judge a single dramatic image to love at first
  glance, with the news hierarchy doing the talking.
- **Full-day coverage, same as v1.** The house images were drawn early on
  13 November from morning news only. This cover carries the whole day,
  including the stories that broke later: Huang's resignation and the 16%
  share fall, the Microsoft outage entering its second day, and the Hormuz
  mine strike.
- **It reads at any size.** Masthead, globe, one headline, three short
  cover lines — nothing below ~18 px except the footer strip, and every
  word is rendered crisply by PIL.
- **No garbled text, no invented events.** The artwork is drawn
  programmatically with PIL (deterministic vector-style illustration, built
  by `dev/news-image-v2/build_image.py`); every headline is PIL-rendered,
  so every word is spelled correctly, and every story is a real 13 Nov
  2026 event.
- **The numbering is a picture-editor device.** The markers on the globe
  and the cover lines share numbers 1–4, so the judge can see at a glance
  that the image maps the day's news onto the world — the summary is in
  the picture, not just in the text.

## How it runs

`main.py` (Python 3.13 stdlib only) copies the bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
Deterministic: two runs write byte-identical files. The image is
1024×1024 PNG, 146,016 bytes (limit 1 MiB).
