import csv

def read_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def print_report(data):
    print("Data Report")
    print("-----------")
    for row in data:
        print(row)

if __name__ == "__main__":
    data = read_data("data.csv")
    print_report(data)
