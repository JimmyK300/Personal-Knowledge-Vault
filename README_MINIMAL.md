# Minimal usage: capture and store notes

Goal: make it trivially easy to record notes and daily entries.

Quick commands:

- Create a daily note (creates Daily/YYYY-MM-DD.md if missing):

```powershell
py .\scripts\new_note.py --daily
```

- Create a quick titled note (saved under `Notes/`):

```powershell
py .\scripts\new_note.py --title "Idea about X"
```

Where files go:

- `Daily/` — daily notes (one per date)
- `Notes/` — general notes created with `new_note.py`
- `Templates/` — templates for structured notes (already present)

Recommended simple routine:

1. Capture quickly with `new_note.py` or drop into `Daily/`.
2. When you feel like tidying, you can move older notes into subfolders (e.g., `Notes/Archive/`) manually.

If you want, I can create a sample note now using the script.
