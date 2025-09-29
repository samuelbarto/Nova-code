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
          <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
          <title>Palmarès Ligue des champions</title>
          <style>
            :root {{
              color-scheme: light dark;
              font-family: 'Roboto', 'Arial', sans-serif;
            }}

            * {{
              box-sizing: border-box;
            }}

            body {{
              margin: 0;
              min-height: 100vh;
              display: flex;
              flex-direction: column;
              align-items: center;
              background: #eef1f5;
              color: #0f172a;
            }}

            header {{
              position: fixed;
              top: 0;
              left: 0;
              right: 0;
              z-index: 100;
              padding: 1.5rem 1rem;
              background: rgba(255, 255, 255, 0.92);
              backdrop-filter: blur(8px);
              box-shadow: 0 8px 24px rgba(15, 23, 42, 0.12);
              text-align: center;
            }}

            header h1 {{
              margin: 0;
              font-size: clamp(1.4rem, 1.6rem + 0.6vw, 2.1rem);
              font-weight: 700;
              letter-spacing: 0.015em;
            }}

            main {{
              width: min(1200px, 100%);
              padding: 7.5rem 1.5rem 3rem;
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 1.75rem;
            }}

            table {{
              width: 100%;
              border-collapse: separate;
              border-spacing: 0;
              background: #ffffff;
              border-radius: 20px;
              padding: 2rem 1.5rem;
              box-shadow: 0 28px 60px rgba(15, 23, 42, 0.15);
            }}

            thead {{
              position: absolute;
              width: 1px;
              height: 1px;
              margin: -1px;
              border: 0;
              padding: 0;
              clip: rect(0 0 0 0);
              clip-path: inset(50%);
              overflow: hidden;
            }}

            tbody {{
              display: grid;
              grid-template-columns: repeat(4, minmax(0, 1fr));
              gap: 1.5rem;
            }}

            tr {{
              display: flex;
              flex-direction: column;
              align-items: center;
              background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
              border-radius: 16px;
              padding: 1.25rem 1rem 1.5rem;
              gap: 0.65rem;
              box-shadow: 0 14px 28px rgba(15, 23, 42, 0.12);
              transition: transform 0.25s ease, box-shadow 0.25s ease;
            }}

            tr:hover {{
              transform: translateY(-4px);
              box-shadow: 0 18px 32px rgba(15, 23, 42, 0.18);
            }}

            td {{
              padding: 0;
              text-align: center;
            }}

            .year {{
              font-weight: 700;
              font-size: 1.1rem;
              letter-spacing: 0.05em;
              color: #1e293b;
            }}

            .club {{
              display: flex;
              justify-content: center;
            }}

            .club-wrapper {{
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 0.75rem;
              color: #0f172a;
            }}

            .club-wrapper img {{
              height: 50px;
              width: auto;
              max-width: 60px;
              object-fit: contain;
              filter: drop-shadow(0 6px 14px rgba(15, 23, 42, 0.25));
              background: #ffffff;
              border-radius: 50%;
              padding: 0.35rem;
            }}

            .club-wrapper span {{
              font-weight: 600;
              font-size: 0.95rem;
              text-align: center;
            }}

            .source {{
              margin: 0;
              text-align: center;
              color: #475569;
              font-size: 0.95rem;
            }}

            @media (max-width: 1200px) {{
              tbody {{
                grid-template-columns: repeat(3, minmax(0, 1fr));
              }}
            }}

            @media (max-width: 900px) {{
              tbody {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
              }}
            }}

            @media (max-width: 600px) {{
              main {{
                padding-top: 8.5rem;
              }}

              tbody {{
                grid-template-columns: 1fr;
              }}
            }}

            @media (prefers-color-scheme: dark) {{
              body {{
                background: #0f172a;
                color: #e2e8f0;
              }}

              header {{
                background: rgba(15, 23, 42, 0.92);
                box-shadow: 0 8px 24px rgba(2, 6, 23, 0.6);
              }}

              table {{
                background: rgba(15, 23, 42, 0.85);
                box-shadow: 0 28px 60px rgba(2, 6, 23, 0.75);
              }}

              tr {{
                background: linear-gradient(180deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
                box-shadow: 0 14px 28px rgba(2, 6, 23, 0.65);
              }}

              tr:hover {{
                box-shadow: 0 18px 36px rgba(2, 6, 23, 0.75);
              }}

              .year {{
                color: #f8fafc;
              }}

              .club-wrapper {{
                color: #e2e8f0;
              }}

              .club-wrapper img {{
                background: rgba(148, 163, 184, 0.2);
                filter: drop-shadow(0 6px 14px rgba(2, 6, 23, 0.6));
              }}

              .source {{
                color: #cbd5f5;
              }}
            }}
          </style>
        </head>
        <body>
          <header>
            <h1>Palmarès de la Ligue des Champions (1956–2023)</h1>
          </header>
          <main>
            <table aria-describedby=\"palmares-source\">
              <thead>
                <tr>
                  <th scope=\"col\">Année</th>
                  <th scope=\"col\">Vainqueur</th>
                </tr>
              </thead>
              <tbody>
                {table_rows}
              </tbody>
            </table>
            <p class=\"source\" id=\"palmares-source\">Source&nbsp;: L'Équipe — palmarès historique de la Ligue des champions.</p>
          </main>
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
