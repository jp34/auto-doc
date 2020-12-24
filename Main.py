from process.Processor import Processor
from convert.Converter import Converter
from collect.Collector import Collector
from write.Writer import Writer

PATH_RAW = './AutoDoc/data/raw/'
PATH_PROCESSED = './AutoDoc/data/processed/'
PATH_TEXT = './AutoDoc/data/text/'
PATH_SHEET = './AutoDoc/Data.xlsx'

TYPE_PNG = '.png'
TYPE_TXT = '.txt'
FILE_RANGE = [800, 1336]
# 1-799 Turned in
# Works till: 899


def main():

    # Pre-process all images from raw folder
        # Input: Raw
        # Output: Processed
    processor = Processor(PATH_RAW, PATH_PROCESSED, FILE_RANGE)
    processor.process()

    # Convert images to text files
    converter = Converter(PATH_PROCESSED, PATH_TEXT, FILE_RANGE)
    converter.convert()

    # Test integrity of data

    # Collect info from text files
    collector = Collector(PATH_TEXT, FILE_RANGE)
    all_people = collector.collect()

    # Write info to
        # Output: Sheet
    writer = Writer(PATH_SHEET)
    for person in all_people:
        writer.write(person)


if __name__ == "__main__":
    main()
