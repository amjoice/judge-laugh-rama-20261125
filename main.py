from pathlib import Path

JOKE = "Deadlines don't scare me; the 4:59 p.m. \"quick question?\" with a screenshot does."

def write_entry() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    write_entry()
