import argparse
import csv
import sys

def convert(args):
    # Read the input CSV file
    with open(args.csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    # Group the data by JLCPCB Part #
    grouped_data = {}
    for row in data:
        part_number = row[args.column]
        if part_number not in grouped_data:
            grouped_data[part_number] = {
                'Comment': row['Value'],
                'Designator': row['Reference'],
                'Footprint': row['Footprint'].split(':')[-1],
                'JLCPCB Part #': part_number
            }
        else:
            grouped_data[part_number]['Designator'] += ',' + row['Reference']

    fieldnames = ['Comment', 'Designator', 'Footprint', 'JLCPCB Part #']
    csv_writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    csv_writer.writeheader()
    for part_number, row in grouped_data.items():
        csv_writer.writerow(row)


def run():
    parser = argparse.ArgumentParser(description='Group CSV data by JLCPCB Part #')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('-c', '--column', default='JLCPCB Part #', help='Override the column name for JLCPCB Part # (default: "JLCPCB Part #")')
    args = parser.parse_args()
    convert(args)


if __name__ == '__main__':
    run()
