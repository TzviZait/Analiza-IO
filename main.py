import re


def write_text():
    with open("my_text.txt","w",encoding='utf-8') as f:
        f.writelines(["Hello world\n",
                "It’s the first exercise in I/O\n",
                "That mean it is number 1\n",
                "Not 2\n",
                 "Not three\n",
                 "It is exciting\n",
                 "And i am all 4 it"])

def red_text():
     with open('my_text.txt', 'r', encoding='utf-8') as file:
        for index, line in enumerate(file, start=1):
            line = line.strip()
            if re.search(r'\d+', line):
                line_number = int(index)  # הופך את מספר השורה ל-int
                print(f"{line_number}. {line}")


def print_line_word_even():
    with open('my_text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            whord_count = len(line.split())
            if whord_count % 2 == 0:
                print(line)

print_line_word_even()