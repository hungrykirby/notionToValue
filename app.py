import csv
import notionImporter
import graphGenerater
import datetime

def main():
  notion = notionImporter.NotionCsvImporter('Untitled.csv')
  graph = graphGenerater.GraphGenerator('motion', None)
  results = notion.convert_csv_to_list()
  graph_data = {'x': [], 'y': []}
  for i in range(len(results)):
    if results[i][2] == -1:
      continue
    graph_data['x'].append(results[i][1])
    graph_data['y'].append(results[i][2])
  if results == False:
    return False
  for r in results:
    print(r)
  # r_d_max = max(results, lambda r: r)
  graph.set_max_min(max(graph_data['x']), 5, min(graph_data['x']), 0)
  graph.create_motion_graph(graph_data['x'], graph_data['y'], True)
  return True

if __name__ == "__main__":
    main()