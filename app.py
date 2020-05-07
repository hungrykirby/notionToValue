import csv
import notionImporter
import graphGenerater
import datetime
import time

def main():
  notion = notionImporter.NotionCsvImporter('Untitled.csv')
  graph = graphGenerater.GraphGenerator('motion', None)
  graph_filled = graphGenerater.GraphGenerator('motion filled', None)
  results = notion.convert_csv_to_list()
  graph_data = {'x': [], 'y': [], 'timestamp': []}
  for i in range(len(results)):
    if results[i][2] == -1:
      continue
    graph_data['x'].append(results[i][1])
    graph_data['y'].append(results[i][2])
    graph_data['timestamp'].append(float(results[i][1].timestamp()))
  if results == False:
    return False
  # r_d_max = max(results, lambda r: r)
  graph.set_max_min(max(graph_data['x']), 5, min(graph_data['x']), 1)
  graph.create_motion_graph(graph_data['x'], graph_data['y'], '1')
  tmp = graph_filled.fill_gap(graph_data['timestamp'], graph_data['y'], 1000000)
  graph_filled.set_max_min((max(graph_data['timestamp'])), 5, min(graph_data['timestamp']), 1)
  graph_filled.create_motion_graph(tmp['x'], tmp['y'], '1000000')
  return True

if __name__ == "__main__":
    main()