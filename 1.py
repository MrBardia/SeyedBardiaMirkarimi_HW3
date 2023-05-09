#!usr/bin/python3

alpha_num_list = [["twenty", "20"],
                      ["nineteen", "19"],
                      ["eighteen", "18"],
                      ["seventeen", "17"],
                      ["sixteen", "16"],
                      ["fifteen", "15"],
                      ["fourteen", "14"],
                      ["thirteen", "13"],
                      ["twelve", "12"],
                      ["eleven", "11"],
                      ["ten", "10"],
                      ["nine", "9"],
                      ["eight", "8"],
                      ["seven", "7"],
                      ["six", "6"],
                      ["five", "5"],
                      ["four", "4"],
                      ["three", "3"],
                      ["two", "2"],
                      ["one", "1"]]


def change_alpha_num(file: str, num_list: list) -> str:
    """change alphabetic numbers to numbers

    Args:
        file (str): input file
        num_list (list): alpha numeric list

    Returns:
        str: file with numeric digits
    """
    content = file.read()

    for i in range(20):
        if num_list[i][0] in content:
            content = content.replace(num_list[i][0], num_list[i][1])
    with open("newZen.txt", "w", encoding="utf-8") as nf:
        nf.write(content) 


def main():
    with open("Zen.txt", "r+", encoding="utf-8") as f:
        change_alpha_num(f, alpha_num_list)

if __name__ == "__main__":
    main()


