import csv

def read_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def generate_report(data):
    total_score = 0

    print("Data Report")
    print("-----------")

    for row in data:
        score = int(row["score"])
        total_score += score
        print(f'{row["id"]} - {row["name"]} - Score: {score}')

    average = total_score / len(data)
    print("-----------")
    print(f"Total records: {len(data)}")
    print(f"Average score: {average:.2f}")

if __name__ == "__main__":
    data = read_data("data.csv")
    generate_report(data)
