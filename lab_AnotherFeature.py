from lab_Utils import read_text, write_text

# Удаляет пустые строки из src и пишет результат в dst
def remove_empty_lines(src, dst):
    content = read_text(src)
    kept = [line for line in content.splitlines() if line.strip()]
    write_text(dst, "\n".join(kept) + "\n")
    return kept


if __name__ == "__main__":
    lines = remove_empty_lines("data.txt", "data_clean.txt")
    print(f"Kept {len(lines)} non-empty lines")