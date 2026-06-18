from pathlib import Path

index = Path('index.html')
if not index.exists():
    raise SystemExit('Run this from the website repo root where index.html exists.')

html = index.read_text(encoding='utf-8')

# Add Foot & Ankle to Conditions dropdown if not already present.
old_dropdown = '<a href="shoulder.html">Shoulder</a><a href="hip.html">Hip</a><a href="knee.html">Knee</a><a href="hand.html">Hand &amp; Wrist</a><a href="sports-medicine.html">Sports Medicine</a><a href="orthobiologics.html">Orthobiologics</a>'
new_dropdown = '<a href="shoulder.html">Shoulder</a><a href="hip.html">Hip</a><a href="knee.html">Knee</a><a href="foot-ankle.html">Foot &amp; Ankle</a><a href="hand.html">Hand &amp; Wrist</a><a href="sports-medicine.html">Sports Medicine</a><a href="orthobiologics.html">Orthobiologics</a>'
html = html.replace(old_dropdown, new_dropdown)

# Replace the existing homepage condition hub section with the V39 version.
start_marker = '<!-- EDITABLE SECTION: CONDITIONS OVERVIEW / CONDITION HUBS -->'
end_marker = '<section class="bg-ice" id="athletics">'
if start_marker in html and end_marker in html:
    start = html.index(start_marker)
    end = html.index(end_marker)
    replacement = start_marker + '\n' + Path('patches/index-v39-condition-section.html').read_text(encoding='utf-8').strip() + '\n'
    html = html[:start] + replacement + html[end:]
else:
    print('Warning: could not find condition section markers. Dropdown was still patched if possible.')

index.write_text(html, encoding='utf-8')
print('V39 index patch applied: Foot & Ankle nav link and updated condition hub section.')
