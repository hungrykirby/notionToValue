import csv
import notionImporter

def main():
  notion = notionImporter.NotionCsvImporter()
  results = notion.convert_csv_to_list()
  for r in results:
    print(r)

if __name__ == "__main__":
    main()