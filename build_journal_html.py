from pathlib import Path
import markdown
md_content = Path('journal.md').read_text(encoding='utf-8')
html_body = markdown.markdown(
    md_content,
    extensions=['fenced_code']
)

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Antara Learning Journal</title>

<style>
body {{
    max-width: 900px;
    margin: auto;
    font-family: Arial;
    line-height: 1.7;
    padding: 40px;
}}
code {{
    background: #f4f4f4;
    padding: 2px 5px;
}}

pre {{
    background: #f4f4f4;
    padding: 15px;
    overflow-x: auto;
}}
</style>

</head>
<body>

{html_body}

</body>
</html>
"""

Path("index.html").write_text(
    html,
    encoding="utf-8"
)

print("Website Generated")