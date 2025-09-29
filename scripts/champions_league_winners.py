"""Generate palmarès tables for the UEFA Champions League winners."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from textwrap import dedent


def load_winners(csv_path: Path) -> list[tuple[str, str]]:
    """Load winners from the CSV file and return a list of (year, winner)."""
    with csv_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row["Year"], row["Winner"]) for row in reader]


def load_logos(csv_path: Path) -> dict[str, str]:
    """Return a mapping from club name to logo URL."""
    with csv_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return {row["Club"]: row["LogoURL"] for row in reader}


def format_text_table(rows: list[tuple[str, str]]) -> str:
    """Return a simple two-column table as a formatted string."""
    if not rows:
        return "No data available"

    year_width = max(len(year) for year, _ in rows)
    winner_width = max(len(winner) for _, winner in rows)
    header = f"{'Année'.ljust(year_width)} | {'Vainqueur'.ljust(winner_width)}"
    separator = f"{'-' * year_width}-+-{'-' * winner_width}"
    body_lines = [
        f"{year.ljust(year_width)} | {winner.ljust(winner_width)}"
        for year, winner in rows
    ]
    return "\n".join([header, separator, *body_lines])


def format_html_table(rows: list[tuple[str, str]], logos: dict[str, str]) -> str:
    """Return an HTML document that lists winners with their club logos."""
    missing_logos = sorted({winner for _, winner in rows if winner not in logos})
    if missing_logos:
        missing = "\n - ".join(["", *missing_logos])
        raise ValueError(
            "Aucun logo trouvé pour les clubs suivants:" + missing
        )

    table_rows = "\n".join(
        dedent(
            f"""
            <tr>
              <td class=\"year\">{year}</td>
              <td class=\"club\">
                <div class=\"club-wrapper\">
                  <img src=\"{logos[winner]}\" alt=\"Logo {winner}\" loading=\"lazy\" />
                  <span>{winner}</span>
                </div>
              </td>
            </tr>
            """
        ).strip()
        for year, winner in rows
    )

    return dedent(
        f"""
        <!DOCTYPE html>
        <html lang=\"fr\">
        <head>
          <meta charset=\"utf-8\" />
          <title>Palmarès Ligue des champions</title>
          <style>
            :root {{
              color-scheme: light dark;
              font-family: 'Segoe UI', 'Roboto', sans-serif;
            }}

            body {{
              margin: 2rem;
              background: #f7f7f7;
              color: #111;
              line-height: 1.6;
            }}

            h1 {{
              text-align: center;
              margin-bottom: 1.5rem;
            }}

            table {{
              width: min(960px, 100%);
              margin: 0 auto;
              border-collapse: collapse;
              background: #fff;
              box-shadow: 0 6px 24px rgba(0, 0, 0, 0.08);
            }}

            thead th {{
              background: #0a192f;
              color: #fff;
              padding: 0.75rem 1rem;
              text-transform: uppercase;
              letter-spacing: 0.08em;
              font-size: 0.85rem;
            }}

            tbody tr:nth-child(even) {{
              background: rgba(10, 25, 47, 0.06);
            }}

            td {{
              padding: 0.65rem 1rem;
              vertical-align: middle;
            }}

            td.year {{
              text-align: center;
              font-weight: 600;
              width: 15%;
              white-space: nowrap;
            }}

            td.club {{
              width: 85%;
            }}

            .club-wrapper {{
              display: flex;
              align-items: center;
              gap: 0.75rem;
            }}

            .club-wrapper img {{
              width: 42px;
              height: 42px;
              object-fit: contain;
              filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.15));
              background: #fff;
              border-radius: 50%;
              padding: 0.25rem;
            }}

            .club-wrapper span {{
              font-weight: 500;
            }}

            .source {{
              margin-top: 1.5rem;
              text-align: center;
              font-size: 0.9rem;
              color: #555;
            }}

            @media (prefers-color-scheme: dark) {{
              body {{
                background: #0a192f;
                color: #e6f1ff;
              }}

              table {{
                background: rgba(2, 12, 27, 0.85);
                box-shadow: 0 12px 30px rgba(2, 12, 27, 0.8);
              }}

              tbody tr:nth-child(even) {{
                background: rgba(100, 255, 218, 0.08);
              }}

              td {{
                border-color: rgba(255, 255, 255, 0.1);
              }}

              .club-wrapper img {{
                background: #e6f1ff;
              }}

              .source {{
                color: #a8b2d1;
              }}
            }}
          </style>
        </head>
        <body>
          <h1>Palmarès de la Ligue des champions (1956-2024)</h1>
          <table>
            <thead>
              <tr>
                <th>Année</th>
                <th>Vainqueur</th>
              </tr>
            </thead>
            <tbody>
              {table_rows}
            </tbody>
          </table>
          <p class=\"source\">Source&nbsp;: L'Équipe — palmarès historique de la Ligue des champions.</p>
        </body>
        </html>
        """
    ).strip()


def build_output_path(path_argument: str | None) -> Path:
    if path_argument:
        return Path(path_argument)
    return Path("outputs") / "champions_league_winners.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Affiche le palmarès de la Ligue des champions au format texte ou "
            "génère un tableau HTML enrichi avec les logos des clubs."
        )
    )
    parser.add_argument(
        "--format",
        choices={"text", "html"},
        default="html",
        help="Format de sortie souhaité (par défaut : html).",
    )
    parser.add_argument(
        "--output",
        help="Chemin du fichier HTML à produire (utilisé uniquement avec --format html).",
    )
    return parser.parse_args()


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    winners_path = repo_root / "data" / "champions_league_winners.csv"
    logos_path = repo_root / "data" / "champions_league_club_logos.csv"

    rows = load_winners(winners_path)

    args = parse_args()
    if args.format == "text":
        print(format_text_table(rows))
        return

    logos = load_logos(logos_path)
    html = format_html_table(rows, logos)
    output_path = build_output_path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Tableau HTML généré dans {output_path}")


if __name__ == "__main__":
    main()
