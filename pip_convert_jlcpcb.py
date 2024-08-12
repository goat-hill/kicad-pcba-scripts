import argparse
import csv
import sys

def convert(args):
    # Open the original CSV file
    with open(args.csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Update the header names based on mappings
    header = data[0]
    column_mappings = {
        'Ref': 'Designator',
        'PosX': 'Mid X',
        'PosY': 'Mid Y',
        'Rot': 'Rotation',
        'Side': 'Layer'
    }
    # Update headers with new column names if they exist in the mappings
    header = [column_mappings.get(col, col) for col in header]
    data[0] = header

    # Write the updated data to stdout
    writer = csv.writer(sys.stdout)
    writer.writerows(data)

def run():
    parser = argparse.ArgumentParser(description='Rename specific columns in a CSV file and output to stdout.')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    args = parser.parse_args()
    convert(args)

if __name__ == '__main__':
    run()
