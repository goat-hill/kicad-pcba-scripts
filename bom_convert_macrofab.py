import argparse
import csv
import sys

def read_bom(bom_file):
    with open(bom_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        bom_data = {row['Reference']: row for row in csv_reader}
    return bom_data

def read_pick_and_place(pnp_file):
    with open(pnp_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        pnp_data = list(csv_reader)
    return pnp_data

def convert_to_xyrs(bom_data, pnp_data):
    xyrs_data = []
    
    for part in pnp_data:
        refs = part['Ref'].split(',')
        for ref in refs:
            if ref in bom_data:
                bom_part = bom_data[ref]
                xyrs_entry = {
                    'Designator': ref,
                    'X-Loc': float(part['PosX']) * 39.3701,  # converting mm to mils
                    'Y-Loc': float(part['PosY']) * 39.3701,  # converting mm to mils
                    'Rotation': int(float(part['Rot'])),
                    'Side': '1' if part['Side'].lower() in ['top', '1'] else '2',
                    'Type': '1' if 'SMD' in bom_part['Footprint'] else '2',
                    'X-Size': '1',  # Placeholder, as actual size is not provided
                    'Y-Size': '1',  # Placeholder, as actual size is not provided
                    'Value': bom_part['Value'],
                    'Footprint': bom_part['Footprint'],
                    'Populate': '1' if not bom_part['DNP'] else '0',
                    'MPN': bom_part['MacroFab Part #']
                }
                xyrs_data.append(xyrs_entry)
    return xyrs_data

def write_xyrs(xyrs_data):
    fieldnames = ['Designator', 'X-Loc', 'Y-Loc', 'Rotation', 'Side', 'Type', 'X-Size', 'Y-Size', 'Value', 'Footprint', 'Populate', 'MPN']
    csv_writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, delimiter='\t')
    print(f"#{'\t'.join(fieldnames)}")
    for row in xyrs_data:
        csv_writer.writerow(row)

def run():
    parser = argparse.ArgumentParser(description='Convert KiCad BOM and Pick and Place files to XYRS format')
    parser.add_argument('bom_file', help='Path to the KiCad BOM CSV file')
    parser.add_argument('pnp_file', help='Path to the KiCad Pick and Place CSV file')
    args = parser.parse_args()
    
    bom_data = read_bom(args.bom_file)
    pnp_data = read_pick_and_place(args.pnp_file)
    xyrs_data = convert_to_xyrs(bom_data, pnp_data)
    write_xyrs(xyrs_data)

if __name__ == '__main__':
    run()
