import csv
import notionImpoter

def main():
  notion = notionImpoter.NotionCsvImpoter()
  results = notion.convert_csv_to_list()
  for r in results:
    print(r)

if __name__ == "__main__":
    main()