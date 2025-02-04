import sys

import markdown


def Convert_MD_HTML(file1, file2):
    with open(file1, 'r') as f1:
        md_content = f1.read()
    html_contents = markdown.markdown(md_content)

    with open(file2, 'w') as f2:
        f2.write(html_contents)

    print(f"Converted {file1} -> {file2}")


def main():
    command = sys.argv[1]  # "markdown"
    input_file = sys.argv[2]  # "test.md" 等
    output_file = sys.argv[3]  # "test.html" 等

    if command == "markdown":
        Convert_MD_HTML(input_file, output_file)


if __name__ == "__main__":
    main()






