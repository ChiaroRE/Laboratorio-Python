from datetime import datetime
def date(file):

  dates = []

  my_file = open(file,"r")
  for line in my_file:
    elements = line.split(",")
    if elements[0] != 'Date':
      try:
        value_t = datetime.strptime(elements[0], '%d-%m-%Y')
        dates.append(value_t)
      except ValueError:
        print("Not a date")
  return dates

file = "shampoo_sales.csv"
dates = date(file)
for data in dates:
  print(data.strftime('%d-%m-%Y'))