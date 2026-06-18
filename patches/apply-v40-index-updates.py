#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply v40 homepage updates to the current index.html.

Usage from the repository root:
  python3 patches/apply-v40-index-updates.py

This replaces the Conditions dropdown contents and the homepage condition hub section.
It creates `index.html.v40-backup` before writing changes.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
index_path = root / "index.html"
backup_path = root / "index.html.v40-backup"

html = index_path.read_text(encoding="utf-8")
backup_path.write_text(html, encoding="utf-8")

nav = '<a href="shoulder.html">Shoulder</a><a href="hip.html">Hip</a><a href="knee.html">Knee</a><a href="foot-ankle.html">Foot &amp; Ankle</a><a href="hand.html">Hand &amp; Wrist</a><a href="sports-medicine.html">Sports Medicine</a><a href="orthobiologics.html">Orthobiologics</a>'
html = re.sub(
    r'(<span class="dropbtn">Conditions</span><div class="dropdown-menu">)(.*?)(</div></div>)',
    lambda m: m.group(1) + nav + m.group(3),
    html,
    count=1,
    flags=re.S,
)

section = '<section id="conditions"><div class="container"><div class="section-head"><h2>Conditions and care areas.</h2><p>These pages are the foundation for patient education on symptoms, diagnosis, non-surgical options, surgery, and recovery expectations.</p></div><div class="condition-grid"><a class="condition-card" href="shoulder.html"><div class="condition-icon">💪</div><h3>Shoulder</h3><p>Rotator cuff tears, shoulder arthritis, instability, fractures, and replacement.</p></a><a class="condition-card" href="hip.html"><div class="condition-icon">🦴</div><h3>Hip</h3><p>Hip arthritis, bursitis, hip pain, injections, and Robotic Hip Replacement.</p></a><a class="condition-card" href="knee.html"><div class="condition-icon">🦵</div><h3>Knee</h3><p>Knee arthritis, meniscus tears, ACL injuries, patellar instability, injections, arthroscopy, and Mako Robotic Knee Replacement.</p></a><a class="condition-card" href="foot-ankle.html"><div class="condition-icon">🦶</div><h3>Foot &amp; Ankle</h3><p>Ankle sprains, Achilles problems, fractures, tendon pain, arthritis, and overuse injuries.</p></a><a class="condition-card" href="hand.html"><div class="condition-icon">✋</div><h3>Hand &amp; Wrist</h3><p>Carpal tunnel, cubital tunnel, trigger finger, hand pain, and fractures.</p></a><a class="condition-card" href="sports-medicine.html"><div class="condition-icon">🏃</div><h3>Sports Medicine</h3><p>Athletic injuries, return-to-play decisions, arthroscopy, and overuse injuries.</p></a><a class="condition-card" href="orthobiologics.html"><div class="condition-icon">🧬</div><h3>Orthobiologics</h3><p>PRP, biologic options, and image-guided treatments where appropriate.</p></a></div></div></section>'
html, n = re.subn(r'<section id="conditions">.*?</section>', section, html, count=1, flags=re.S)
if n != 1:
    raise SystemExit("Could not replace the homepage conditions section. Restore from backup and patch manually.")

index_path.write_text(html, encoding="utf-8")
print("v40 index updates applied. Backup saved to index.html.v40-backup")
