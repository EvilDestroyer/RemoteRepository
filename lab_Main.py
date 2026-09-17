from utils import read_text, write_text, count_lines

if __name__ == "__main__":
    write_text("data.txt", "Hello, Git!\n")
    lineAmount = count_lines("data.txt")
    write_text("data.txt", count_lines + " <- This is the number of lines in file!\n")
    print(read_text("data.txt"))