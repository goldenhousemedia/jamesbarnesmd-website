# JamesBarnesMD.com v40 knee build

## What is included

This package is structured so the contents can be copied into the repository root.

- `knee.html` — rebuilt knee page using the uploaded knee images.
- `foot-ankle.html` — placeholder-level foot and ankle page carried forward from v39.
- `assets/photos/knee/` — optimized JPG website assets from the uploaded knee images.
- `assets/photos/foot-ankle/` — placeholder folder for future foot/ankle assets.
- `assets/logos/convergence-health-wordmark.svg` — simple Convergence Health text badge placeholder.
- `patches/` — cleaned homepage/index update tools.

## Important cleanup from v39 patches

The v39 package had multiple index patch snippets. v40 streamlines this into:

1. `patches/apply-v40-index-updates.py` — one optional script that updates the Conditions dropdown and homepage Conditions hub.
2. `patches/nav-conditions-dropdown-v40.html` — manual nav snippet.
3. `patches/index-condition-section-v40.html` — manual homepage condition hub snippet.

Because the full live `index.html` was not safely available inside the container, I did not generate a full replacement `index.html`. That is intentional to avoid overwriting the homepage with an incomplete file. Use the script or snippets after pulling the current repo locally.

## Recommended upload flow

1. Copy `knee.html` into the repo root.
2. Copy `foot-ankle.html` into the repo root.
3. Copy `assets/photos/knee/` into `assets/photos/knee/`.
4. Copy `assets/logos/convergence-health-wordmark.svg` into `assets/logos/`.
5. Apply the index update using `python3 patches/apply-v40-index-updates.py` from the repo root, or manually add Foot & Ankle to the Conditions dropdown and homepage condition grid.

## Image note

The fracture X-ray review image had mock patient text and a nameplate artifact. I cropped the optimized website version to reduce the issue. It is acceptable as a lower-page image, but I would regenerate it later without any visible patient/doctor text artifacts.
