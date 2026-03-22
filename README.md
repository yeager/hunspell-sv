# hunspell-sv 🇸🇪

Modern Swedish dictionary for Hunspell spell checking.

## Stats

| Metric | Value |
|--------|-------|
| **Dictionary entries** | 154,476 |
| **Base** | SFOL 2.42 (Den Stora Fria Ordlistan) |
| **Added from TM** | 762 compound words & technical terms |
| **TM source** | 776,274 translation memory entries |
| **License** | LGPL-3.0 |

## Sources

- **[SFOL 2.42](https://sfol.se/)** — The main Swedish open source dictionary by Göran Andersson (LGPL-3.0)
- **Translation Memory** — 559,792 unique source strings from professional Swedish translations across:
  - GNOME, KDE, LibreOffice, Mozilla
  - Ubuntu, Fedora, Debian
  - Weblate, Transifex, Crowdin
  - 50+ open source projects

## What's different from the standard sv_SE?

The standard `sv_SE.dic` in most Linux distros and LibreOffice is from 2016-2017. This dictionary:

1. **Starts from SFOL 2.42** (2020) — 1,500+ more words than the distro version
2. **Adds 762 compound words** verified in professional translations (appearing ≥5 times in TM)
3. **Focuses on software/technical Swedish** — terms translators actually use

### Example words added

```
lösenfras, meddelandekö, symlänk, filbläddrare, åsidosättning,
fjärrvärd, trädvy, skogshuggartält, datakällobjekt, rasterkarta,
vertexfärg, färgramp, proxyinställningar, ångringshistorik
```

## Installation

### Manual (any OS)
```bash
# Copy to hunspell dictionary path
sudo cp sv_SE.dic sv_SE.aff /usr/share/hunspell/
```

### macOS (Homebrew hunspell)
```bash
cp sv_SE.dic sv_SE.aff /opt/homebrew/share/hunspell/
```

### Personal dictionary (no root needed)
```bash
mkdir -p ~/Library/Spelling  # macOS
cp sv_SE.dic sv_SE.aff ~/Library/Spelling/
```

## Contributing

Found a Swedish word that's missing? Open an issue or PR!

The best way to contribute:
1. Translate open source software to Swedish
2. Your translations feed into translation memory
3. New words are automatically extracted and added

## Building from source

```bash
python3 build.py  # Merges SFOL + TM additions
```

## License

LGPL-3.0 — same as SFOL/DSSO upstream.
