# JamesBarnesMD.com Editing Guide

This site is organized so you do **not** need to replace the entire website every time you make a change.

## Main files

- `index.html` — Homepage only.
- `shoulder.html` — Shoulder condition hub.
- `hip.html` — Hip condition hub.
- `knee.html` — Knee condition hub.
- `hand.html` — Hand and wrist condition hub.
- `sports-medicine.html` — Sports medicine hub.
- `orthobiologics.html` — Orthobiologics hub.
- `assets/styles.css` — Shared visual styling for all pages.
- `assets/` — Photos and other media.

## How to edit without starting over

### To change homepage text
Edit only `index.html`. Look for comments such as:

- `EDITABLE SECTION: WHY PATIENTS CHOOSE DR. BARNES`
- `EDITABLE SECTION: CONDITIONS OVERVIEW / CONDITION HUBS`
- `EDITABLE SECTION: PHOTO GALLERY`
- `EDITABLE SECTION: REVIEWS`
- `EDITABLE SECTION: CONTACT + LOCATION`

### To change colors, spacing, buttons, fonts, or mobile layout
Edit only:

`assets/styles.css`

### To build out individual condition pages
Edit the specific file:

- Shoulder content → `shoulder.html`
- Hip content → `hip.html`
- Knee content → `knee.html`
- Hand content → `hand.html`
- Sports medicine content → `sports-medicine.html`
- PRP/BMAC/orthobiologics content → `orthobiologics.html`

### To add a new condition page later
1. Duplicate the most similar file, such as `shoulder.html`.
2. Rename it, for example: `rotator-cuff-tear.html`.
3. Edit the title, meta description, headline, and content.
4. Add the new link to the Conditions dropdown in each page's top navigation.

## Upload strategy for GitHub

You do not need to upload the whole zip every time.

- If only one page changes, upload/replace only that one `.html` file.
- If design changes, upload/replace only `assets/styles.css`.
- If images change, upload/replace only the specific image file in `assets/`.


## v10 notes
- Community section photo is `assets/community-flag.jpg`.
- Review count is intentionally not displayed to avoid constant manual updates.
- To change review text, edit the `patient-quotes` block in `index.html`.
