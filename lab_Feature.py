from lab_Utils import read_text

# Функция для сбора статистики строк, слов и символов в файле
def text_stats(path):
    content = read_text(path)
    lines = content.splitlines()
    words = content.split()
    chars = len(content)
    return {"lines": len(lines), "words": len(words), "chars": chars}


if __name__ == "__main__":
    stats = text_stats("data.txt")
    print("Statistics for data.txt:")
    for key, value in stats.items():
        print(f"  {key}: {value}")