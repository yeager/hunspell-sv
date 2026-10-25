# Changes

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
