import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "champions_league_club_logos.csv"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "public" / "champions_league_table.html"

TABLE_STYLE = """
body {
    font-family: Arial, sans-serif;
    background-color: #f5f7fa;
    padding: 2rem;
}

table {
    width: 100%;
    border-collapse: collapse;
    background-color: #ffffff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

thead th {
    background-color: #1a237e;
    color: #ffffff;
    padding: 12px;
    text-align: left;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.85rem;
}

tbody td {
    padding: 12px;
    border-bottom: 1px solid #e0e0e0;
    vertical-align: middle;
}

tbody tr:nth-child(even) {
    background-color: #f0f3ff;
}

td img {
    height: 48px;
    width: auto;
}

@media (min-width: 768px) {
    table {
        max-width: 960px;
        margin: 0 auto;
    }
}
"""


def build_table(rows):
    header = "<thead><tr><th>Année</th><th>Club</th><th>Logo</th><th>Pays</th></tr></thead>"
    body_cells = []
    for row in rows:
        year, club, logo, country = row
        body_cells.append(
            "<tr>"
            f"<td>{year}</td>"
            f"<td>{club}</td>"
            f"<td><img src=\"{logo}\" alt=\"Logo {club}\"></td>"
            f"<td>{country}</td>"
            "</tr>"
        )
    body = "<tbody>" + "".join(body_cells) + "</tbody>"
    return "<table>" + header + body + "</table>"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Le fichier CSV est introuvable: {DATA_PATH}")

    with DATA_PATH.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # skip header
        rows = list(reader)

    table_html = build_table(rows)
    page_html = f"""
<!DOCTYPE html>
<html lang=\"fr\">
<head>
    <meta charset=\"utf-8\">
    <title>Clubs vainqueurs de la Ligue des champions</title>
    <style>{TABLE_STYLE}</style>
</head>
<body>
    <h1>Clubs vainqueurs de la Ligue des champions</h1>
    <p>Tableau généré automatiquement à partir du fichier CSV <code>champions_league_club_logos.csv</code>.</p>
    {table_html}
</body>
</html>
"""

    OUTPUT_PATH.write_text(page_html, encoding="utf-8")


if __name__ == "__main__":
    main()
