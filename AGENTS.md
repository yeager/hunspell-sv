# Svenska språkregler

Använd alltid Språkrådet (Isof) som förstahandskälla vid nya eller ändrade
svenska språkregler och skrivregler. Följ `docs/sprakpolicy.md`: kontrollera
aktuellt källstöd, dokumentera direkta hänvisningar och bevara accepterade
varianter. SAOL kompletterar för enskilda ord enligt Språkrådets hänvisningar.

Gör inte kontextberoende skrivråd till generella stavningsförbud. Uppdatera
regelunderlag och relevanta regressioner tillsammans. Kör
`python3 -m unittest discover -s tests -v` före inlämning.
