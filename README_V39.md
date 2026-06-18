# James Barnes MD website v39 package

This package includes:

- `knee.html` — fully expanded knee page outline/content using existing site classes and placeholder image paths.
- `foot-ankle.html` — new placeholder-level foot and ankle page, similar in scope to the current hip placeholder page.
- `assets/photos/knee/README.md` — exact filenames expected by the knee page.
- `assets/photos/foot-ankle/README.md` — exact filename expected by the foot/ankle placeholder page.
- `KNEE_IMAGE_PROMPTS.md` — recommended prompts for the knee images.
- `patches/index-v39-condition-section.html` — replacement condition hub section for the homepage.
- `patches/nav-conditions-dropdown-v39.html` — nav dropdown snippet with Foot & Ankle added.
- `patches/apply-v39-index-patch.py` — optional helper script to patch the current homepage index file.

## Install notes

1. Copy `knee.html` into the repo root, replacing the existing knee page.
2. Copy `foot-ankle.html` into the repo root.
3. Copy the `assets/photos/knee/` and `assets/photos/foot-ankle/` folders into the same asset paths in the repo.
4. Add generated image files using the exact filenames listed in the README files.
5. Patch `index.html` by either:
   - manually adding `foot-ankle.html` to the Conditions dropdown and replacing the condition hub section with `patches/index-v39-condition-section.html`, or
   - running `python patches/apply-v39-index-patch.py` from the repo root after copying the `patches` folder.

No CSS file is included because the pages intentionally reuse existing classes from the shoulder, sports medicine, hip, and knee pages.
