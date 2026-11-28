# hunspell-sv 2026.11.28

Adds reviewed Home Assistant product names and technical vocabulary to both Swedish Hunspell dictionaries, including `Halvgradssteg`, `Helgradssteg`, `returkod` and `certifikatutfärdarfilen`. Regression coverage includes the checked compounds, product spellings and inflections.

Validation: 19/19 unit tests pass. Hunspell accepts the full reviewed HA Core batch except the `.p8` file extension, which is intentionally preserved.
