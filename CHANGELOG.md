- Add the verified Swedish compounds `Duntvätt`, `vinklingstid`, `dimningsnivå` and `Fasstyrning` to both dictionaries and spelling regressions after Home Assistant Core review showed valid UI compounds being flagged. No second package release created because 2026.11.26 was released earlier today.
- Add the recommended plural `emojier` and recognize `emoji` as a Swedish compound part; add Hunspell regressions. Evidence: [Isof Frågelådan](https://frageladan.isof.se/faqs/30678). No package release created because the 2026.11.26 release was already made today.
- Add the Homee smart-home brand and reviewed compound `homee-enheten` to both dictionaries and spelling regressions after the HA Core review exposed a false positive. No package release created because the 2026.11.26 release was already made today.
- Add reviewed Home Assistant Core sound-label vocabulary to both dictionaries and spelling regressions: `sci-fi` compound support, `hissklocka`, `sonarsignal`, `slädbjällror` and `susljud`. SAOL supports `susljud`; Home Assistant review verifies the UI labels, and the Swedish Maritime Administration documents `bogvåg`. No package release created because the 2026.11.26 release was already made today.
- Add the valid MQTT compounds `fläktlägeskommando` and `svänglägeskommando`, including plurals, after the HA Core review exposed false positives.
- Add reviewed Home Assistant terms and device labels, including Namecheap DynamicDNS, HDFury HDMI identifiers, CO₂, befuktning and laddsession.
- Add reviewed Home Assistant term “upptäckbar” and SMA Solar proper noun after spell-check false positives.
- Add the reviewed Home Assistant brands `Tibber`, `OpenAI` and `Proxmox` to both dictionaries and the proper-noun reference after spell-check false positives.
# Changes

## 2026.11.25

- Add the KNX Association Swedish term `datapunkttyp` (plural `datapunkttyper`) after an official KNX string exposed a Hunspell false positive; add Home Assistant technical product names and TTS to both dictionaries with spelling regressions. The user-approved compounds `USB-dongel` and `usb-dongel` are covered.

## 2026.11.26

- Add the valid compound `installatörskod` and its forms, `utfasad` and its forms, and the Jewish Calendar names Adot Mizrah, Ashkenaz, Nusach, Omer and Sfarad to both dictionaries and spelling regressions. The Home Assistant [Count the Omer action](https://www.home-assistant.io/actions/jewish_calendar.count_omer/) defines the specialist names; SAOB documents `fasa ut` and the participle `utfasad` ([utfasa](https://svenska.se/?q=utfasa)).
- Add Home Assistant product names, including Google Cast, technical abbreviations and their API compounds after the Core review exposed valid UI terms as Hunspell false positives; add spelling regressions.
- Add `avlarmat` and its inflections, coffee term `förbryggning` and unit `rpm` after the Core review exposed them as valid Swedish UI words.

- Add `nivålås` and its inflections, plus Ohme, Reolink and Snoo names and common Home Assistant compounds to both dictionaries and spelling regressions.

- Add `sviträknare` and its common inflections after the Home Assistant Habitica review exposed this valid compound as a Hunspell false positive.

- Add reviewed Home Assistant product names, MQTT/SSDP terminology and IronOS model names to the proper-noun reference and both dictionaries; cover their UI compounds in spelling regressions.

- Add `moppningsrutt` and `rumsnamn` with inflections to both dictionaries and spelling regressions after Home Assistant map and room-label review.

- Add `checklistpunkt` and `lödspets` with common inflections to both dictionaries and spelling regressions after Home Assistant Core review exposed valid compound false positives.

- Add the correct Swedish Habitica terms `uppgiftsalias` and the inflections `aliaset` and `uppgiftsaliaset` to both dictionaries and spelling regressions after the HA Core review exposed false positives.

- Add the valid Home Assistant compounds `eco-läge` and `hysteresläge` to both Hunspell dictionaries and spelling regressions after the ZHA review flagged them.

- Add the established Swedish UI term `turboläge` to both dictionaries and the regression corpus after its reviewed Home Assistant label was flagged; the Swedish Philips user manual uses “Turboläge” as a mode label: https://www.documents.philips.com/assets/20210423/20de1b38309546b1b9c6ad13011f08ed.pdf.

- Add the KNX volume-delta term `deltavolym` to both dictionaries and spelling regressions, supported by the Swedish [Philips TV user manual](https://www.documents.philips.com/assets/20250224/2cc56a9eadf44ed7b20db28e002d808e.pdf) which uses *deltavolym* for a volume adjustment.

- Add Home Assistant air-quality identifiers `PM1`, `PM2`, `PM4`, `PM10` and `VOC` to Hunspell with spelling regressions after KNX device-class review.

- Add the KNX abbreviation `DPT` and its Swedish genitive and compound forms after Core strings showed the Hunspell dictionary was flagging it; add regressions.

- Add the official Home Assistant brand spelling `VELUX` to Hunspell after its gateway name was flagged in the Core review; add a spelling regression.

- Add technical term `hysteresband`, complete the `börvärde` inflections, and add VELUX model `KLF200` with gateway compound regressions after Home Assistant Core review exposed false spelling warnings. Evidence: [LTH measurement material](https://bme.lth.se/fileadmin/biomedicalengineering/Courses/Maetteknik_foer_E_D/Tid_och_Frekvens_2018_del_1.pdf) uses `hysteresband`; [VELUX](https://www.velux.com/klf200) identifies KLF 200 as its interface model.


- Add the valid compound `växelriktarström`, supported by Viessmann's Swedish term `växelriktare`, and the Home Assistant product name `WaterFurnace` with its hyphenated Swedish compound `WaterFurnace-tjänsten`; add spelling regressions for the Home Assistant Core review.
- Add the established compound push-uppdateringar to both dictionaries after a Home Assistant CoIoT review exposed a Hunspell coverage gap. Evidence includes existing Home Assistant translation-memory use and an independent occurrence in [Ubuntu DDTP Swedish translations](https://github.com/yeager/translations/blob/main/translations/ubuntu-ddtp/ddtp-ubuntu-universe-sv.po); add a spelling regression.
- Add the established Swedish technical term `standardindata` to both dictionaries and spelling regressions after Home Assistant Core review; the equivalent is used in [Microsoft Learn’s Swedish .NET documentation](https://learn.microsoft.com/sv-se/dotnet/api/system.diagnostics.processstartinfo.standardinputencoding?view=net-5.0).
- Add the established Swedish compound `nedladdningskö` to both Hunspell dictionaries and the spelling regression corpus, supported by Swedish user documentation from [Synology](https://global.download.synology.com/download/Document/Software/UserGuide/Firmware/DSM/4.3/sve/Syno_UsersGuide_NAServer_sve.pdf) and [Suunto](https://www.suunto.com/sv-se/Support/faq-articles/suunto-app/how-can-i-download-offline-maps-to-my-suunto-watch/).

- Add Swedish technical term `mired`, the HA term `blueprint` and `utgångskod`, plus Home Assistant integration/vendor names exposed during Core review; add spelling regressions. Mired usage follows [Nikon Swedish documentation](https://chsv-origin-onlinemanual.nikonimglib.com/zf/sv/white_balance_36.html), and `utgångskod` follows the reviewed Home Assistant term memory.
- Add `Modbus` and the Azure Speech proper names `Guangxi`, `Henan`, `Jilu`, `Shaanxi`, `Türkiye`, `Wu` and `Zhongyuan` to the Swedish Hunspell dictionaries, with regressions for reviewed compounds.
- Add `Modbus` as a Home Assistant protocol name to the Swedish Hunspell dictionaries; regression-check `Modbus-hubben`, the established spelling already present in HA translation memory.
- Add the Swedish language names `kannada`, `malayalam`, `marathi`, `odia`, `sundanesiska` and `telugu` after the Home Assistant voice-locale review. Their spellings are supported by [NE on Kannada and Malayalam](https://www.ne.se/uppslagsverk/skola/avancerad/kannada), [NE on Marathi](https://www.ne.se/uppslagsverk/skola/avancerad/marathi), [NE on Odia/Oriya](https://www.ne.se/uppslagsverk/skola/avancerad/oriya) and [NE on Sundanesiska](https://www.ne.se/uppslagsverk/skola/avancerad/sundanesiska); all six are covered by spelling regressions.
- Add the established Swedish IT term `dongel` after a localization review exposed a dictionary coverage gap; cite [Computer Sweden IT-ord](https://it-ord.computersweden.se/category/elektronisk-kommunikation/telekom/telefoni/mobilt/page/49/) and cover singular and plural forms in both dictionaries.
- Add the established inflections of `API-token` exposed by the Home Assistant review to both dictionaries and the spelling regression corpus.
- Add the Swedish language name `assamesiska` after the Microsoft voice-locale review, supported by [NE](https://www.ne.se/uppslagsverk/skola/avancerad/assamesiska).

## 2026.11.16

- Add reviewed Blender action-slot terms and compositing terminology.
- Publish the current dictionary as the 2026.11.16 package release.

## 2026.10.25

- Package the current reviewed Swedish dictionary for PyPI installation.
- Include the latest reviewed RetroArch video terminology.

## 2026.10.24.4

- Add the reviewed video term `kromakanal` from RetroArch PC-FX.

## 2026.10.24.3

- Add the reviewed display term `bildrutefrekvens` from RetroArch Boom3.

## 2026.10.24.2

- Add reviewed RetroArch terminology for audio output, resampling, mapping and Doom rendering.

## 2026.10.24.1

- Add reviewed storage and audio terminology from RetroArch quasi88.

## 2026.10.24

- Add reviewed Swedish audio and signal-processing terminology from RetroArch QuickNES.

## 2026.10.23.2

- Add reviewed gaming terms `bildrutsöverhoppning` and `nedbromsning` from the RetroArch review.

## 2026.10.23.1

- Add the reviewed Swedish graphics terms `kromaticitet` and `skuggningspass`,
  found during RetroArch localization review.

## 2026.09.21.1

- Make Språkrådet the primary authority for language and writing rules.
- Replace the project-specific one-through-nine preference with contextual
  advice from Språkrådet; add five unscored examples for numeric expressions.
- Validate rule sources and prevent context-only rules from becoming word
  corrections or spelling tests. Dictionary contents are unchanged.
- Ship the language policy and rule catalogue in Debian and RPM packages.

## 2026.09.21

- Correct reviewed explicit misspellings, including formattera, bollliknande
  and skatttefria; retain explicit forbidden entries where necessary.
- Correct enspann to the neuter ABD inflection class; test its full paradigm.
- Validate 187 sourced word cases without tokenization, retaining accepted
  variants and separating grammar/style examples from spelling checks.
- Cover Swedish consonant deletion, including reduced and hyphenated forms.
- Record 17 reviewed corrections for consumers that also import older lists.
- Include 35 rule topics with primary references in docs/svenska-regler.md.

The catalogue is a curated regression source, not a complete Swedish grammar.

## Unreleased

- Add verified Home Assistant terms for Reolink speech volume, PoolDose, MQTT payloads, and reviewed Alexa sound labels to both Swedish Hunspell dictionaries and the regression corpus.

- Added Home Assistant spellings `bayesiansk`, `bayesianska`, and `kodformat`, plus Niko Home Control brand tokens.

- Added Home Assistant KNX terms and test coverage for `jalusiet`, `brytaktor`, `dimmeraktor`, `läsbegäran`, `timerlarm`, and industry-used `gateways`; recognized DALI, GroupValueRead, HSV, OAuth, OTP, RGBW, and XYY identifiers.

- Added Home Assistant Core vocabulary: `datapunktstyp`, `inverterläge`, `jalusiets`, `jalusiställdon`, and `smartlast`.

- Add the Reolink camera term `linjekorsning`, the compounds `intrångsdetektering` and `uppspelningskö` with inflections, and the product name `Pterodactyl`; add spelling regressions after Home Assistant Core review. `uppspelningskö` is supported by the Swedish FOSS term bank entry “Add to Play Queue” → “Lägg till i uppspelningskö”.
- Add reviewed Home Assistant terms and valid compounds for Husqvarna Automower (`geostaket`, `slingsensor`, `slingsignal`, `fällningssensor`, cutting-height labels), plus the product names PlayStation, Opower and GeoFence. No package release created because the 2026.11.26 release was already made today.
- Add the reviewed Tesla preconditioning compounds and Home Assistant webhook forms; recognize Coinbase, Cloud and Sleep in preserved brand names.
- Allow `engångs` outside compounds by correcting its Hunspell flags; the prior entry incorrectly marked it compound-only.
- Add reviewed HA vocabulary for disk-life messages, OneWire input channels, Fyta plant thresholds, electrical RMS labels, Foscam, and related protocol names and compounds.
- Add `extruder` and its common forms/compound regression to both dictionaries after the HA Core review found that Hunspell rejected `Extrudertemperatur`. RISE uses *extruder* as Swedish technical terminology for 3D-printing equipment ([RISE: 3D-printing](https://www.ri.se/sv/berattelse/3d-printing-viktig-del-i-industrins-digitalisering)). No package release created because the 2026.11.26 release was already made today.

- Add `torrent` and its established inflections (including `torrenter`) to both dictionaries after Home Assistant Core review identified the missing Swedish FOSS term; add regression coverage.

- Add the Airobot brand and `Airobot-termostat` compound to both dictionaries and regression coverage after HA Core review found a false positive. No additional package release created today.

- Add verified Home Assistant compounds `växelriktareffekt` and `växelriktartemperatur` to both dictionaries and spelling regressions.

- Add the lowercase `ntfy` brand, Swedish compound `ntfy-ämne`, and the valid Miele compound `Kylningsfas` to both Hunspell dictionaries and regression words after Home Assistant review.

- Add the verified Swedish electrical compound `fasförskjutningsfel`, NRGkick and uHoo brand spellings, and their reviewed Swedish compounds to both dictionaries and regression words after Home Assistant review.

- Add Cloudflare, Prana and the reviewed compounds `Cloudflare`/`Prana-enhet`/`S3-kompatibel` to Hunspell dictionaries and regression words after Home Assistant review.

- Add `förbikoppling` and its sentence-case form to cover a valid Home Assistant HVAC term flagged during Core review.

- Add BTHome compound forms found in Home Assistant Core review to both dictionaries and regression words.

- Add Home Assistant Core HVAC, queue, and product-name compounds found during review to dictionaries and regression words.

- Add Ghost, SmartTub, and SocialWeb product terms and compounds from Home Assistant Core review.

- Add IntelliClima, Globalping, and PTZ/SIP forms found in Home Assistant Core review.

- Add Homevolt/Victron phase and lock-slot terms found in Home Assistant Core review.

- Add Immich, Splunk, AQI/MIME and 24-hour measurement terms from Home Assistant Core review.

- Add Home Assistant Microsoft Entra and appliance terms plus Swedish app-registration compounds.

- Add IDrive e2 product identifier and compounds.

- Add Mastodon product-name compounds found in Home Assistant Core review.

- Add Advantage Air, Daikin, Hypontech, Indevolt, MTA and SmartThings vocabulary from Home Assistant Core review.

- Add the reviewed Home Assistant compound `utomhusläge` and its inflections after Hunspell flagged a Swedish mode label; add a regression case. No package release created because the 2026.11.26 release was already made today.
