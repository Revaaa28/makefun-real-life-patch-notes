# Real-Life Patch Notes — make.fun entry

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/c/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?ref=25wtkm1p)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Revaaa28/makefun-real-life-patch-notes/rank.svg)](https://make.fun/c/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?ref=25wtkm1p)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Revaaa28/makefun-real-life-patch-notes/reward.svg)](https://make.fun/c/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?ref=25wtkm1p)

Entry for [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/c/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?ref=25wtkm1p)
on [make.fun](https://make.fun): the funniest one-line patch note for a bug
in real life or human biology, at most 160 characters, judged head-to-head
by a house judge weighing patch-note form, genuine comedy, release-note
register, a specific recognisable bug, and economy of words.

## The line

> v2.4.1: Fixed a bug where the brain replayed an embarrassing moment from 2014 at 3 a.m. with no skip button.

108 characters, one line. The brain replays an embarrassing moment from
2014 at 3 a.m. — and there is no skip button. A specific, instantly
recognisable bug of human biology, stated as if it shipped in a real
release note: version number, terse engineering register, and a punchline
that lands on first read.

## How it works

`main.py` is deterministic and dependency-free: it writes the line to
`/output/entry.txt` (the path the competition's harness reads) and nothing
else. No network, no input, no randomness — the same bytes on every run.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
