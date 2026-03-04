#!/usr/bin/env python3
"""Create a quick note or daily note.

Usage examples:
  # create a normal note with title
  py .\scripts\new_note.py --title "My idea about X"

  # create today's daily note (opens or creates Daily/YYYY-MM-DD.md)
  py .\scripts\new_note.py --daily

This is intentionally minimal: creates a markdown file with small YAML frontmatter.
"""
import os
import argparse
import datetime
import re


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9\- ]+", "", s)
    s = s.replace(" ", "-")
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def create_daily():
    date = datetime.date.today().isoformat()
    dirpath = os.path.join(ROOT, "Daily")
    ensure_dir(dirpath)
    path = os.path.join(dirpath, f"{date}.md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("---\n")
            fh.write(f'title: "{date} Daily"\n')
            fh.write(f"date: {date}\n")
            fh.write("tags: [daily]\n")
            fh.write("type: daily\n")
            fh.write("status: active\n")
            fh.write("---\n\n")
            fh.write("# " + date + " Daily\n\n")
            fh.write("## 1 Priority\n\n")
    return path


def create_note(title):
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    slug = slugify(title) or "note"
    dirpath = os.path.join(ROOT, "Notes")
    ensure_dir(dirpath)
    filename = f"{slug}-{now}.md"
    path = os.path.join(dirpath, filename)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("---\n")
        fh.write(f'title: "{title}"\n')
        fh.write(f"date: {datetime.date.today().isoformat()}\n")
        fh.write("tags: []\n")
        fh.write("type: resource\n")
        fh.write("status: active\n")
        fh.write("---\n\n")
        fh.write("# " + title + "\n\n")
    return path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--daily", action="store_true", help="Create/open today daily note")
    p.add_argument("--title", "-t", help="Title for a quick note")
    args = p.parse_args()

    if args.daily:
        path = create_daily()
        print("Daily note:", path)
        return

    if args.title:
        path = create_note(args.title)
        print("Created note:", path)
        return

    # interactive fallback
    title = input("Note title (leave empty to create daily): ").strip()
    if not title:
        path = create_daily()
        print("Daily note:", path)
    else:
        path = create_note(title)
        print("Created note:", path)


if __name__ == "__main__":
    main()
