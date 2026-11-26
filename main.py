import os

LINE = "Tomorrow in Drizzleford: light rain, heavy sarcasm, and a 100% chance the forecast apologizes by noon."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
