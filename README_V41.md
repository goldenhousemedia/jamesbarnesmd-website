# JamesBarnesMD.com v41 clean knee/index build

## What changed

- Full replacement `index.html` is included now, so the previous v39/v40 patch workflow is removed.
- `knee.html` is rebuilt with the knee image set and now includes the arthritic knee vs Stryker Triathlon Knee System illustration.
- `foot-ankle.html` remains included as a clean placeholder page.
- Knee images are included under `assets/photos/knee/`.
- A simple Convergence Health wordmark SVG is included under `assets/logos/` and referenced from the homepage and footer.

## Patch cleanup

There is no `patches/` folder in this build. The index changes are already incorporated into `index.html`:

- Conditions dropdown includes Foot & Ankle.
- Homepage condition grid includes Foot & Ankle.
- Homepage joint replacement section uses the knee arthritis/Stryker Triathlon comparison image.
- Convergence branding is included in the location section and footer.

## Upload flow

Copy the contents of this folder into the repository root and commit. This package is intended to be a clean upload, not a patch overlay.

## Image note

The arthritic knee/Triathlon comparison image is placed in the knee replacement/arthritis section and also used on the homepage joint replacement panel. The prior fracture X-ray review image still has minor mock text/nameplate artifacts; it is retained as a lower-page image but should eventually be regenerated cleanly.
