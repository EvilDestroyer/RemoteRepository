from utils import read_text, write_text

if __name__ == "__main__":
    write_text("data.txt", "Hello, Git!\n")
    print(read_text("data.txt"))