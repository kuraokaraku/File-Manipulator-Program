import sys

def reverse_file(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        contents = f.read()
    reverse_contents = contents[::-1]
    with open(outputpath, 'w') as f:
        f.write(reverse_contents)
    print(f"逆順ファイルを作成しました: {outputpath}")

def copy_file(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)
    print(f"ファイルをコピーしました: {outputpath}")

def duplicate_file(inputpath, n):
    with open(inputpath, 'r') as f:
        contents = f.read()
        duplicate_contents = contents * n
    with open(inputpath, 'w') as f:
        f.write(duplicate_contents)
    print(f"{inputpath} の内容を {n} 回複製して上書きしました。")

def replace_file(inputpath, needle, newstring):
    with open(inputpath, 'r') as f:
        contents = f.read()
    with open(inputpath, 'w') as f:
        f.write(contents.replace(str1, str2))
    print(f"{inputpath} の '{needle}' を '{newstring}' に置き換えました。")

def main():
    command = sys.argv[1]

    if command == "reverse":
        reverse_file(sys.argv[2], sys.argv[3])

    elif command == "copy":
        copy_file(sys.argv[2], sys.argv[3])

    elif command == "duplicate-contents":
        duplicate_file(sys.argv[2], sys.argv[3])

    elif command == "replace-string":
        replace_file(sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == "__main__":
    main()





