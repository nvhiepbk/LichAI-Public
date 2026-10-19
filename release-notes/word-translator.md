## Lịch AI Word Translator 1.0.1 · 2026-10-19

# Lịch AI Word Translator

## v1.0.1 — release candidate

- Windows portable EXE for DOCX translation.
- Two modes: full-document translation and page-interleaved bilingual output (Microsoft Word required for the latter).
- Sentence-level translation log with one-line shortened previews.
- Pause/resume controls and per-sentence checkpoint file.
- Handles HTTP 429 by stopping rather than hammering the translation endpoint.

### Requirements and caveats

- Requires Internet; translation service may rate-limit requests.
- Page interleaving requires Microsoft Word installed on the user's Windows machine.
- Complex formatting, tables, headers/footers, and pagination must be reviewed manually.
- Sensitive documents may be sent to third-party translation endpoints; obtain appropriate authorization before use.

### Publication gate

Do not announce a public release until Windows CI, the downloadable EXE, and the real Word page-pairing acceptance test have passed. The Word release metadata is separate from the Excel translator's assets.
