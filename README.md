# hunspell-sv 🇸🇪

Modern Swedish dictionary for Hunspell spell checking.

## Stats

| Metric | Value |
|--------|-------|
| **Dictionary entries** | 166,794 |
| **Base** | SFOL 2.42 (Den Stora Fria Ordlistan) |
| **Added from TM** | 11,552 words (≥3 occurrences) |
| **Added Datatermgruppen** | 50 IT/tech terms |
| **Added SAOL 15** | 43 new words (2026) |
| **Added proper nouns** | 105 software/brand/place names |
| **Added custom terms** | 556 from review work |
| **Added compound morphemes** | 47 for better compound support |
| **TM source** | 784,147 translation memory entries |
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
2. **Adds 12,000+ new words** from multiple sources:
   - 11,552 from translation memory (≥3 occurrences)
   - 50 IT terms from Datatermgruppen 
   - 43 new words from SAOL 15 (2026)
   - 105 proper nouns (software, brands, places)
   - 556 custom review terms
   - 47 compound morphemes
3. **Improves compound support** — better handling of Swedish compound words
4. **Focuses on modern Swedish** — includes contemporary terms from translations, social media, and official sources

### Example words added

```
TM words: lösenfras, meddelandekö, symlänk, filbläddrare, åsidosättning,
fjärrvärd, trädvy, skogshuggartält, datakällobjekt, rasterkarta,
vertexfärg, färgramp, proxyinställningar, ångringshistorik

Datatermgruppen: adressikon, bluffwebbplats, funktionalitet, 
gränssnittskomponent, spionprogram, tjock klient, vinkelkompensering

SAOL 15: incel, matfattigdom, menstrosa, prompta, tippningspunkt,
influencer, klimatångest, digitalisering, kryptovaluta, hashtag

Proper nouns: Ubuntu, LibreOffice, systemd, Docker, Kubernetes,
Stockholm, Göteborg, Microsoft, Google, PostgreSQL
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
