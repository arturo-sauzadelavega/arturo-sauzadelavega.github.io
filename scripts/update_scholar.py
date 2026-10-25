import json
import sys
import datetime
from pathlib import Path
from scholarly import scholarly

SCHOLAR_ID = "HGBJ7qkAAAAJ"
OUT = Path(__file__).resolve().parent.parent / "data" / "scholar.json"

try:
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics", "indices", "counts"])
except Exception as e:
    print(f"Cannot obtain data from Google Scholar: {e}")
    print("Keeping previous data.")
    sys.exit(0)

per_year = [
    {"year": int(y), "citations": int(c)}
    for y, c in sorted(author.get("cites_per_year", {}).items())
]

# Si la respuesta viene vacía, no sobrescribimos los datos buenos
if not per_year:
    print("Empty response from Google Scholar. Using previous data.")
    sys.exit(0)

data = {
    "total_citations": author.get("citedby", 0),
    "h_index": author.get("hindex", 0),
    "i10_index": author.get("i10index", 0),
    "per_year": per_year,
    "updated": datetime.date.today().isoformat(),
    "profile_url": f"https://scholar.google.com/citations?user={SCHOLAR_ID}",
}

OUT.write_text(json.dumps(data, indent=2))
print(f"Updated data: {data['total_citations']} total citations.")
