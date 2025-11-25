# arxiv-daily-scroll

Fetch the latest arXiv papers for selected categories, generate concise Chinese highlights with DeepSeek, and publish a static site to GitHub Pages automatically.

## What this repo does
- Pull recent arXiv papers for the tags in `tags.json` (default: `cs.CV`, `cs.RO`).
- Call DeepSeek to produce a one-line headline, three bullet points, and keywords in Chinese.
- Save raw metadata + AI summaries under `data/YYYY-MM-DD/`.
- Build a GitHub Pages-ready site under `docs/` with per-day indexes and per-paper pages.

## Project layout
- `main.py`: Fetch today’s arXiv window and generate AI summaries.
- `build_page.py`: Turn data into a multi-day Jekyll site (outputs to `docs/`).
- `utils/`: ArXiv querying, DeepSeek prompt logic, and helpers.
- `data/`: Dated outputs (`arxiv.json`, `ai_summary.json` per day).
- `docs/`: Generated site; set as GitHub Pages source.
- `.github/workflows/daily.yml`: CI that runs daily and pushes updates.

## Local quickstart
1) Install deps (Python 3.10+):
```bash
pip install -U arxiv openai tqdm requests python-dateutil
```
2) Set your DeepSeek API key:
```bash
export DEEPSEEK_API_KEY=your_key
```
3) (Optional) adjust categories in `tags.json`.
4) Fetch & summarize today:
```bash
python main.py
```
5) Build the site to `docs/`:
```bash
python build_page.py --data data --outdir docs --title "arXiv·cs.CV 中文要点汇总（with DeepSeek）"
```
Open `docs/index.html` locally, or push and enable GitHub Pages (see below).

## GitHub Actions setup (auto daily build + Pages deploy)
The workflow `.github/workflows/daily.yml` is already included. To wire it up:
1) Add a repo secret `DEEPSEEK_API_KEY` (Settings → Secrets and variables → Actions → New repository secret).
2) Enable Actions on the repo if disabled.
3) Configure Pages: Settings → Pages → Source = your default branch (e.g., `main`) and folder `docs/`.
4) (Optional) Edit the cron in `daily.yml` (`30 4 * * *` UTC ≈ 12:30 Beijing) or tweak tags/title/env.
5) Trigger manually (Actions → “Daily arXiv cs.CV fetch & build” → Run workflow) or wait for the schedule.

What the workflow does:
- Check out the repo, install Python deps.
- Run `main.py` to fetch today’s arXiv window and call DeepSeek with the secret key.
- Run `build_page.py` to regenerate `docs/`.
- Commit and push changes (new data + site). Pages will serve from `docs/` automatically.

## Configuration tips
- Categories: edit `tags.json`.
- Prompts: `utils/prompts/system.txt` and `utils/prompts/user.txt`.
- Concurrency/temperature: `update_ai_summary_async` in `utils/analyser.py`.
- Site title/output dirs: CLI flags in `build_page.py`.

## Data outputs
- `data/YYYY-MM-DD/arxiv.json`: raw arXiv metadata (title, authors, arXiv ID, abstract).
- `data/YYYY-MM-DD/ai_summary.json`: same items plus `headline_zh`, `intro_zh`, `tags_zh`; model errors are recorded for debugging.
- `docs/`: static site (Jekyll-compatible) with daily index and per-paper pages.

## License
GPL-3.0. See `LICENSE`.
