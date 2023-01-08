import argparse
import ast


def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return 1-current_row[n]/(len(str_1)+len(str_2))


def text():
    parser = argparse.ArgumentParser()
    parser.add_argument('indir')
    parser.add_argument('outdir')
    args = parser.parse_args()
    ou = open(f"{args.outdir}", "w")
    with open(f"{args.indir}") as inp:
        for line in inp:
            both_files = line.split()
            with open(both_files[0]) as txt_one:
                s_1 = txt_one.read()
                str_1 = ast.dump(ast.parse(s_1))
            with open(both_files[1]) as txt_two:
                s_2 = txt_two.read()
                str_2 = ast.dump(ast.parse(s_2))
            ou.write(str(levenstein(str_1, str_2)))
            print(levenstein(str_1, str_2))
    ou.close()


if __name__ == '__main__':
    text()

