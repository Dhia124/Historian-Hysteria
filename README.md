# Historian Hysteria

A small Python project with solutions to coding puzzle challenges. Day 1 focuses on "Historian Hysteria", with additional days included.

## Project Structure
- `day1_part1.py` — Solution for Day 1, Part 1
- `day1_part2.py` — Solution for Day 1, Part 2
- `day2.py` — Solution for Day 2
- `day3.py` — Solution for Day 3
- `day4.py` — Solution for Day 4
- `input.txt`, `input2.txt`, `input3.txt`, `input4.txt` — Example puzzle inputs

## Requirements
- Python 3.10+ recommended
- No third‑party dependencies (standard library only)

## Running
From the repository root, run any script:

```bash
python day1_part1.py
python day1_part2.py
python day2.py
python day3.py
python day4.py
```

Each script expects a corresponding `input*.txt` file in the repo. If your inputs use different filenames, update the scripts or rename your files accordingly.

## Notes
- Solutions are intentionally simple and focused on clarity.
- If you find bugs or have improvements, feel free to open an issue or PR.

## Publish to GitHub
Once you’re ready to push this repo (including the README) to GitHub:

```bash
git init
git add README.md *.py input*.txt
git commit -m "Add README and puzzle solutions"
git branch -M main
git remote add origin <your_repo_url>
git push -u origin main
```