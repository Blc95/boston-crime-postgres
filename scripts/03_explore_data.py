import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = BASE_DIR / "data" / "boston.csv"

def get_col_set(csv_filename, col_index):
    col_set = set()

    with open(csv_filename) as f:
        csv_f = csv.reader(f)
        next(csv_f)

        for row in csv_f:
            col_set.add(row[col_index])

    return col_set


def get_unique_count_for_each_col(header_row):
    number_of_unqie_values_on_columns = dict()
    for col in range(len(header_row)):
        number_of_unqie_values_on_columns[header_row[col]] = len(get_col_set(CSV_PATH, col))

    return number_of_unqie_values_on_columns
  
def get_max_len_of_description():
    max_len = 0
    col_set = get_col_set(CSV_PATH, 2)
    for crime in col_set:
        len_of_crime = len(crime)
        if len_of_crime > max_len:
            max_len = len_of_crime
    return max_len


def main():
    with open(CSV_PATH) as f:
        csv_f = csv.reader(f)
        header_row = next(csv_f)
        number_of_unique_values_on_columns = get_unique_count_for_each_col(header_row=header_row)
        print(number_of_unique_values_on_columns)
        max_len = get_max_len_of_description()
        print(max_len)
    

if __name__ == "__main__":
    main()    