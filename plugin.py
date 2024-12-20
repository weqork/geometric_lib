import os 

def add_newline_to_print(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        if 'print' in line:
            updated_line = process_print_line(line)
        else:
            updated_line = line
        updated_lines.append(updated_line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)


def process_print_line(line):
    result = ''
    i = 0
    in_string = False
    quote_type = ''

    while i < len(line):
        if line[i:i+6] == 'print(':
            result += 'print('
            i += 6
            inside_print = True
        elif inside_print:
            if line[i] in ('"', "'"):
                if not in_string:
                    in_string = True
                    quote_type = line[i]
                    result += line[i]
                elif in_string and line[i] == quote_type:
                    result += '\\n' + line[i]
                    in_string = False
                else:
                    result += line[i]
            elif in_string:
                result += line[i]
            else:
                result += line[i]
            if line[i] == ')':
                inside_print = False
        else:
            result += line[i]
        i += 1

    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    if os.path.isfile(args.path):
        add_newline_to_print(args.path)
    else:
        print('invalid pytb')
