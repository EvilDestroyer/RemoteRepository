def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text(path, content="No text was supplied"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def count_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)