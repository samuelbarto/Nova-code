"""Display the UEFA Champions League winners by season from 1956 onwards.

The data is stored in ../data/champions_league_winners.csv and is derived from
L'Équipe's historical palmarès reference for the European Cup/Champions League.
"""

from __future__ import annotations

import csv
from pathlib import Path


def load_winners(csv_path: Path) -> list[tuple[str, str]]:
    """Load winners from the CSV file and return a list of (year, winner)."""
    with csv_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row["Year"], row["Winner"]) for row in reader]


def format_table(rows: list[tuple[str, str]]) -> str:
    """Return a simple two-column table as a formatted string."""
    if not rows:
        return "No data available"

    year_width = max(len(year) for year, _ in rows)
    winner_width = max(len(winner) for _, winner in rows)
    header = f"{'Année'.ljust(year_width)} | {'Vainqueur'.ljust(winner_width)}"
    separator = f"{'-' * year_width}-+-{'-' * winner_width}"
    body_lines = [f"{year.ljust(year_width)} | {winner.ljust(winner_width)}" for year, winner in rows]
    return "\n".join([header, separator, *body_lines])


def main() -> None:
    data_file = Path(__file__).resolve().parent.parent / "data" / "champions_league_winners.csv"
    rows = load_winners(data_file)
    print(format_table(rows))


if __name__ == "__main__":
    main()
