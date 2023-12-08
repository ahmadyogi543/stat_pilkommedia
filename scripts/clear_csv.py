import csv
import io


def clear_comma(text):
    csv_reader = csv.reader(io.StringIO(text))
    rows = list(csv_reader)

    # Replace commas with periods in each element of the rows
    for i, row in enumerate(rows):
        rows[i] = [value.replace(',', '.') for value in row]

    # Convert the modified rows back to a CSV-formatted string
    output_text = io.StringIO()
    csv_writer = csv.writer(output_text)
    csv_writer.writerows(rows)
    result = output_text.getvalue().strip()

    return result


INPUT_PATH = "statistik_iwak_papuyu.csv"
OUTPUT_PATH = "statistik_iwak_papuyu_clear.csv"

with open(INPUT_PATH, mode='r', encoding='utf-8') as r:
    lines = r.readlines()
    with open(OUTPUT_PATH, mode='w+', encoding='utf-8') as w:
        for line in lines:
            w.write(clear_comma(line) + "\n")

print("DONE")
