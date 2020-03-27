from datetime import datetime
import re
import os
import csv

FIN_PATH = os.path.join('.', 'transcript.txt')
FOUT_PATH = os.path.join('.', 'transcription.csv')

p = re.compile('^[0-9]*:[0-9]{2}')


def parse_ts(line_data):
    timestamp = p.findall(line_data)

    if timestamp:
        return True, timestamp[0]

    return False, None


def itterlines(filename):
    """read raw lines from a textfile"""
    row_index = 0
    record = {}
    with open(filename, 'r') as fin:
        for row_data in fin:
            if row_index % 500 == 0 and row_index > 0:
                print(f'Parsed {row_index} lines')

            record = process_row_data(row_data, record)
            record = process_append(record)
            row_index += 1


def record_is_valid(record):

    has_timestamp = 'timestamp' in record.keys()
    has_word_data = 'word_data' in record.keys()

    if has_timestamp and has_word_data:
        return True
    return False


def process_append(record):
    if record_is_valid(record):
        append_dict_as_row(FOUT_PATH, record)
        record = {}
    return record


def append_dict_as_row(file_name, record_dict):

    with open(file_name, 'a+', newline="") as fout:
        fieldnames = ['timestamp', 'word_data']
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writerow(record_dict)


def process_row_data(row_data, record):
    row_data = row_data.rstrip('\n\r')

    is_ts, ts_value = parse_ts(row_data)

    if row_data == '':
        pass

    elif is_ts:
        # make new record
        record['timestamp'] = ts_value

    else:
        # update existing record
        record['word_data'] = row_data

    return record


def main():
    itterlines(FIN_PATH)


if __name__ == "__main__":
    main()
