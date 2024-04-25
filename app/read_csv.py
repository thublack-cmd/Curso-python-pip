import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

def read_world_popu(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = []
    country = []
    for row in reader:
      country.append(row[2])
      data.append(row[16])
    country.pop(0)
    data.pop(0)
    return country, data

if __name__ == '__main__':
  #data = read_csv('./app/data.csv')
  data = read_world_popu('./app/data.csv')
  print(data[0])