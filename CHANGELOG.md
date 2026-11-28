## 2026.11.28

## Unreleased

- Add Swedish increment terms `Halvgradssteg` and `Helgradssteg`, the established technical term `returkod`, the valid compound `certifikatutfärdarfilen`, and reviewed Home Assistant product names to both Hunspell dictionaries. Add regressions for the checked spellings and inflections.

- Add KNX feature name `Secure` to the curated proper-noun list and both Hunspell regression dictionaries after HA Core review found the feature label flagged. No package release created.

- Add reviewed Home Assistant proper nouns (`Aqara`, `Croma`, `Finder`, `Glances`, `Magic`, `Twinkly`, `SoH`, and SmartThings `Developer Center`) plus valid Swedish compound `ersättningsapp` to both dictionaries and regression coverage. No package release created.

- Add reviewed Home Assistant integration names (`AEMET`, `AdGuard`, `BLUETTI`, `Foreca`, `Jellyfin`, `Seafile`, `Solyx`, `RainbowMiner`, and related branded compounds) to Hunspell and regression coverage. No package release created.

- Add the valid Home Assistant weather compounds `vindbyhastighet` and `radarreflektivitet` to both Hunspell dictionaries and spelling regression coverage after Core review found them flagged as unknown words. The terms are correct in their component context; no package release created.

- Add validated LIFX theme vocabulary and proper names, including `Kwanzaa`, `Menora`, `lo-fi`, `Leprechaunens`, `Pumpafest` and `Pumpakrydda`, to both dictionaries and spelling regressions. `Menora` matches the reviewed FOSS termbank: https://github.com/yeager/swedish-foss-terminology/blob/main/termbank-flat.csv. Swedish `lo-fi` usage is documented by Region Värmland: https://regionvarmland.se/download/18.6410fb76186b9ec35181eaf9/1679038973706/Temablad%2520fr%25C3%25A5n%2520Mediecenter%2520V%25C3%25A4rmland%2520-%2520Musik.pdf. `Kwanzaa` and the retained cultural names come from the reviewed Home Assistant LIFX theme catalog: https://www.home-assistant.io/integrations/lifx. `Old Glory` remains an unresolved proper-name signal. No package release created.

- Add `Chanukka` and `chanukka` to both dictionaries and spelling regressions; add title-case `Chanukka` to the proper-noun inventory after LIFX review identified a false Hunspell flag. Isof recommends lowercase `chanukka` in running text; the UI label keeps the project’s title-style capitalization. Source: https://frageladan.isof.se/faqs/31011. No package release created.

- Add verified Home Assistant device names, protocols and compounds, including DSM, DVR, gRPC, MOSFET, NAS and SofarCloud vocabulary, plus Swedish proxy inflections and `växelriktarläge`, to Hunspell regressions. No additional package release created today.

- Add the Swedish compound `linjekod` and its inflections to both dictionaries and regression coverage after Home Assistant Core review exposed it as a false Hunspell flag. No additional tool release created today.

- Add the established Swedish chemistry term `redoxpotential` to both dictionaries and spelling regressions after Home Assistant Core review flagged it. Add verified Core proper nouns and compounds `iZone`, `Météo-France`, `TCL`, `Fitbit`, `Health`, `IPS`, `Homematic`, `INDI`, `Allsky` and Home Assistant’s `resruttinställning` forms to both dictionaries and regression coverage. Primary reference: https://www.folkhalsomyndigheten.se/publikationer-och-material/publikationsarkiv/v/vagledning-om-bassangbad/?pub=86245. No second tool release created today.


- Add X10 and Zigbee technology names with their HA connectivity compounds to both Hunspell dictionaries, proper-noun inventory and regressions after the Core review exposed false positives. Primary references: [X10 home automation](https://www.x10.com/pages/allaboutx10), [CSA Zigbee standard](https://csa-iot.org/all-solutions/zigbee/). No package release created.

- Add `vitruvianske` to both Hunspell dictionaries and spelling regressions. Source: [Nationalmuseum on the Vitruvian Man](https://www.nationalmuseum.se/assets/Dokument/Skolan/Om%C3%B6jliga-kroppar.pdf). No package release created.

- Add verified Home Assistant protocol and service names plus recurring `mopptvätt` vocabulary to both Hunspell dictionaries, proper-noun inventory and spelling regressions. Primary references: [GS1 Sweden on GTIN](https://gs1.se/guider/kom-igang-guider/kom-igang-skapa-streckkod/), [DECT Forum](https://www.dect.org/technologies/dect-ule/), [EnOcean](https://www.enocean.com/en/technology/radio-technology/), [Apple on HomeKit](https://support.apple.com/en-om/guide/security/sec3a881ccb1/web), [Connectivity Standards Alliance on Matter](https://csa-iot.org/all-solutions/matter/matter-faq/), and [Picnic](https://picnic.app/de/ueber-picnic/). No package release created.

- Add `aktiveringslås` and its definite forms after HA Core review found the established Apple Swedish term missing from Hunspell. Source: https://support.apple.com/sv-se/108794. No package release created.

- Add reviewed Home Assistant product and router terms, contextually valid compounds and `autentiseringsapp` inflections, plus the DNS record compound `SRV-posten`, `PSK` and `PSK-autentisering`, plus the Swedish device term `vippbrytare` to both Hunspell dictionaries and spelling regressions. No package release created.

- Add `dataexfiltrering` to both dictionaries and spelling regressions; Swedish FOSS terminology records it at 100% confidence.

- Add `smartmätargateway` and its definite form, verified in Home Assistant Core translations.
- Add the Swedish terms `sirén`, `rumsprioritet` and `solcellsväxelriktare` found during Home Assistant Core review.
- Add the verified compound `larmwebhook`.
- Add the definite forms `tokenen` and `åtkomsttokenen`.
- Add reviewed Home Assistant vocabulary: `hydroponik`, `vattenavhärdare`, `utomhusluftkvalitet`, `hemhubbar` and `pushnotiser` with inflections.
- Add `moppbricka` and its common inflections.

- Add SmartyPlants, WiZ, Acmeda and Rejseplanen product forms plus Swedish `pollning` inflections after HA Core review exposed Hunspell coverage gaps. No additional release created today.
- Add Threema and SwitchBot names and the reviewed `SwitchBot-appen` compound to both Hunspell dictionaries and spelling regressions. No additional release created today.
- Add the Insteon product name and its reviewed Home Assistant compound to both Hunspell dictionaries and spelling regressions. No additional release created today.
- Add Gemini product-name compounds and Swedish inflections of `alias` after HA Core review exposed dictionary coverage gaps; add regressions. No additional release created today.
- Add reviewed KNX term `datapunkttyp` and its common inflections to both dictionaries and regression coverage after HA Core review exposed false positives. No additional release created today.
- Add the Imou brand forms and the reviewed compound `apphemlighet` with inflections after HA Core review exposed false Hunspell flags. No additional release created today.
- Add reviewed smart-lock term `fallkolv` and keyboard event compound `tangentnedhållning` plus inflections to both Hunspell dictionaries and regression coverage after HA Core review found false positives. No second package release created today.
- Add verified LaMetric, LiteLLM, Hydrawise, Starlink, Sofar and LIFX compounds plus `baudhastighet` and `blippa` inflections to both dictionaries and regression coverage after Core review exposed valid terms as Hunspell false positives. No package release created today.
- Add reviewed ENGIE, Electric Kiwi, MELCloud, Portainer, SQLite and Belgium proper-name vocabulary after Home Assistant Core review exposed valid product names as Hunspell false positives. No package release created today.
- Add reviewed KNX, ETS, DPT and XKNXProject terms after Home Assistant Core review exposed valid technical names as Hunspell false positives. No package release created today.
- Add verified Swedish astronomy, shell and Home Assistant terminology plus Bedrock, Legacy, Vitesy Hub, Zonneplan, ADU, SQM and SELV vocabulary to both dictionaries and regression coverage after Core review exposed false positives. No package release created today.
- Add verified NeoPool, Duco, Zonneplan and EnergyID terms (including hysteresis, tariff group and WebRTC compounds) to both dictionaries and spelling regressions after HA Core review exposed valid vocabulary as false positives. No package release created today.
- Add validated HA camera/KNX terms, HEV LED terminology and LIFX/myStrom brand compounds to both dictionaries and regression vocabulary after Core review exposed false positives. No package release created today.
- Add the verified Swedish camera term `binningläge` to both dictionaries and regression vocabulary after HA Core review exposed a valid technical compound as a Hunspell false positive. No package release created today. Evidence: https://www.tucsen.com/sv/dhyana-2100-product/
- Add valid Swedish `gatewayen` and keep `hexsträng` available in the expanded dictionary; add regression vocabulary after HA Core review exposed missing Hunspell entries. No second package release created today.
- Add LibreNMS, Silla/Prism, PM0 and the reviewed Home Assistant compound `midnattsolsperioden` to Hunspell dictionaries and regression coverage after a Core review exposed false positives. No package release created today.
- Add Home Assistant vocabulary `Auto`, `Bortaläge`, `Ethernet`, `Laddningsfaser`, `NexBlue`, `Wi-Fi`, `Sugfläkt`, `rökgasställdon` and `märkström` after Hunspell review exposed valid terms as false positives; cover capitalization and NexBlue compounds. No package release created today.
- Fix Hunspell tokenization of subscript numerals in hyphenated compounds by adding Unicode subscript digits to `WORDCHARS` in both dictionaries; add `CO₂-halt` and `CO₂-halten` regressions. No second package release created today.
- Add the verified Bosch `VarioPerfect` and Victron `BatteryLife`/`PowerAssist` feature names to Hunspell dictionaries and regression words after Home Assistant Core review. No package release created today.
- Add the verified electrical compound `fasföljdslarm` to both dictionaries and spelling regressions after HA Core review exposed a valid term that Hunspell incorrectly flagged. No additional release created today.
- Add the lowercase form `bulkfas` and the technical acronym `MPPT` to both dictionaries and spelling regressions after Victron GX review exposed valid Swedish/technical terms that Hunspell flagged. No additional release created today.
- Add the reviewed technical compound `råstatus` to both dictionaries and spelling regressions after HA Core review exposed it as a valid label that Hunspell incorrectly flagged. No release created.
- Add the verified Victron term `bulkladdning`, its state label `Bulkfas`, and the `BMS` acronym to both dictionaries and spelling regressions after HA Core review exposed them as valid technical terms. No second package release created today.
- Add UniFi, Roth and Touchline proper nouns with a `Touchline-styrenhet` regression after HA Core review exposed valid product names as Hunspell false positives. No second package release created today.
- Add `multirumsgrupp`, `bulletschack`, `V1-API`, `V1-API:t`, `Lichess-API-token` and the Glow proper noun with regression tests after HA Core review exposed false positives. No second package release created today.
- Add the WiiM and Growatt brand names and spelling regressions for `WiiM:s`, `WiiM-mediaspelare` and `Growatt-enhet` after HA Core review exposed valid product terms as false positives. No second package release created today.
- Add the `Ollama` proper noun and support its `Ollama-integrationen` and `Ollama-API-nyckel` compounds after HA Core review exposed valid product terminology as Hunspell false positives. No second package release created today.
- Add `LMS` and `Whisker` to the proper-name vocabulary, plus reviewed Swedish compounds `nödlåsning` and `väckningsord`, after Home Assistant Core review exposed valid terms as Hunspell false positives. Add regression cases for `LMS-servrar` and related forms. No second package release created today.
- Add the Swedish Home Assistant audio terms `surroundkanal` and `surroundkanaler` to both dictionaries and spelling regressions. No second package release created today.
- Add the terminology-bank term `Dubbelmono` to both dictionaries and spelling regressions after the HA Core review exposed this valid audio term as a false positive. No second package release created today.
- Add the Enphase measurement abbreviation and reviewed HA product names `CT`, `Last-CT`, `Produktions-CT`, `EVSE-CT`, `Poweropti`, `Satel` and `Integra` to both dictionaries and regressions after Core review exposed false positives.
- Add the valid Swedish terms `kodtolkning` and `mätstatus` to both dictionaries and spelling regressions after the Home Assistant Core review exposed false positives. No second package release created today.
- Add the Powerfox brand and reviewed compound `Powerfox-tjänsten` to both dictionaries and spelling regressions after historic HA strings were flagged. No second package release created today.
- Add Fully and Sonarr proper nouns and the reviewed compound `Sonarr-post` to both dictionaries and regressions after HA Core review exposed false positives. No second package release created because 2026.11.26 was released earlier today.
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

- Add Swedish pet-feeder terminology `foderautomat` and `utfodringsschema`, inflections, and the Tuya brand after the HA Core review found misleading literal translations; add regression coverage.

- Add `laddeffekt` inflections and the Russound brand/compound after HA Core review; add spelling regression coverage.

- Add the TLS acronym to the curated vocabulary after HA Core review flagged the correct compound `TLS-handskakningen`; add regression coverage. No second package release created today.

- Add the attested Swedish plural `gatewayer` and definite plural `gatewayerna` after HA Core review flagged them; [EU legislation uses “gatewayer”](https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX%3A02014R1305-20180316), and Språkrådet recommends checking usage when an uncommon loanword is absent from dictionaries ([Frågelådan 48498](https://frageladan.isof.se/faqs/48498)). Add both forms to regression words.

- Add Home Assistant Core brand/acronym spellings and valid compounds: AFI, EPEX, MPP, PAC, RCD, ROCOF, SteamVR, Powador-protect, `plausibilitetsfel` and `maskinvaruöverström`. Manufacturer/product forms are verified against [KACO Powador-protect](https://kaco-newenergy.com/products/powador-protect), [EPEX SPOT](https://www.epexspot.com/) and [SteamVR Base Station](https://www.vive.com/eu/accessory/base-station2/). Add spelling regression words. No package release created today.

- Add reviewed Home Assistant electrical and RS485 terminology (`mättransformator`, `nätrelä`, `reläspänning`, `ödriftsfel`, hardware overtemperature, relay test and RS485 compounds) to both dictionaries and regression words.

- Add `ödrift`, a valid HA Core island-operation state label, to both dictionaries and regression words.

- Add Home Assistant Core printer cartridge terms, the scanner compound, and AnyList/LoRaWAN/OKOK/Plugwise/SenseCAP/Uptime Kuma names and compounds to both dictionaries and regression words.

- Add Home Assistant holiday-category adjectives and Belgian pharmacy identifier spellings, plus ESPHome/OpenThread/Farmad/Mijn Farmad Apotheek proper names and the reviewed compound `ESPHome-enhet` to both dictionaries and regression words.

- Add the genitive form `gatewayens` to the Swedish dictionaries and regression vocabulary after review flagged a valid technical compound. No package release created.

- Add verified Home Assistant proper nouns `Broadlink` and `Honeywell`, including their reviewed compounds and genitives, to dictionaries and regression vocabulary. No package release created.

- Add reviewed Swedish compounds `klådfrekvens` and `utetemperaturgivare`, plus NAD proper-name spelling and compound, to both dictionaries and regression vocabulary. No package release created.

- Add Tile product name and its Home Assistant compounds and inflections to both dictionaries and regression vocabulary. No package release created.

- Add reviewed Swedish pollen compounds `alpollen`, `askpollen` and `gråbopollen` to both dictionaries and regression vocabulary. No package release created.

- Add the reviewed Swedish compound `mikronätsdrift` to both dictionaries and regression vocabulary after Home Assistant Core review identified the valid term. No package release created.
