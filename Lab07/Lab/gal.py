# gal.py

from pathlib import Path


def read_gal(path: str) -> dict[int, list[int]]:
    """Read Lab07-1.gal and return {unit_id: [neighbor_ids]}.

    Format (for this lab):
    - First line: header (ignored)
    - Then repeated blocks of 2 lines:
        line A: <unit_id> <neighbor_count>
        line B: <neighbor_id_1> <neighbor_id_2> ...
    """

    gal: dict[int, list[int]] = {}

    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 1

    while i < len(lines):
        header_parts = lines[i].split()
        unit_id = int(header_parts[0])

        neighbors = list(map(int, lines[i + 1].split()))
        gal[unit_id] = neighbors

        i += 2

    return gal


def neighbor_histogram(gal: dict[int, list[int]]) -> dict[int, list[int]]:
    """Return {k: [unit_ids]} where k is the number of neighbors."""

    hist: dict[int, list[int]] = {}

    for unit_id, neighbors in gal.items():
        k = len(neighbors)
        hist.setdefault(k, []).append(unit_id)

    return hist


def has_asymmetry(gal: dict[int, list[int]]) -> bool:
    return len(find_asymmetries(gal)) > 0


def find_asymmetries(gal: dict[int, list[int]]) -> list[tuple[int, int]]:
    """Return a list of (i, j) where i lists j, but j does not list i."""

    asym: list[tuple[int, int]] = []

    for i, neighbors in gal.items():
        for j in neighbors:
            if i not in gal.get(j, []):
                asym.append((i, j))

    return asym


if __name__ == "__main__":
    gal_file = Path(__file__).with_name("Lab07-1.gal")

    gal = read_gal(str(gal_file))
    print("Number of units:", len(gal))
    print("First 5 items:", list(gal.items())[:5])

    hist = neighbor_histogram(gal)
    print("Neighbor counts (k):", sorted(hist.keys()))

    asym = find_asymmetries(gal)
    print("Number of asymmetries:", len(asym))
    print("First 10 asymmetries:", asym[:10])
