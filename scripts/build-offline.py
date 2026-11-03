from pathlib import Path
import base64
root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text()
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>' + (root / 'style.css').read_text() + '</style>')
for name in ['engine.js', 'app.js']:
    html = html.replace(f'<script src="{name}"></script>', '<script>' + (root / name).read_text() + '</script>')
html = html.replace('assets/dice-roll.mp3', 'data:audio/mpeg;base64,' + base64.b64encode((root / 'assets/dice-roll.mp3').read_bytes()).decode())
html = html.replace('assets/dice-roll.mp4', 'data:video/mp4;base64,' + base64.b64encode((root / 'assets/dice-roll.mp4').read_bytes()).decode())
html = html.replace('<a href="TBJ-offline.html" download>Download offline HTML ↓</a>', '<span>Offline edition</span>')
(root / 'TBJ-offline.html').write_text(html)
