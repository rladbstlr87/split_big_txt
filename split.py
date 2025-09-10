# 텍스트로만 8메가 정도 되는 txt파일을 split하는 함수

def split_text_by_episode(input_file, output_dir):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    parts = text.split("Episode ")

    # 0번째는 Prologue
    if parts[0].strip():
        with open(f"{output_dir}/Episode_0.txt", "w", encoding="utf-8") as out:
            out.write(parts[0].strip())
        print("Saved Episode_0.txt")

    # 1번째부터는 Episode n
    for i, part in enumerate(parts[1:], start=1):
        filename = f"{output_dir}/Episode_{i}.txt"
        with open(filename, "w", encoding="utf-8") as out:
            out.write("Episode " + part)
        print(f"Saved {filename}")

if __name__ == "__main__":
    split_text_by_episode("big_text.txt", "episodes")