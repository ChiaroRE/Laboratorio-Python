def sum_csv(file):

  values = []
  
  my_file = open(file, 'r') 
  
  for line in my_file:
    elements = line.split(',')

    if elements[0] != 'Date':
      try:
        value_t = float(elements[1])
        values.append(value_t)
      except ValueError:
        print("Not a float")
      
  for item in values:
    print("{}".format(item))

  if(len(values) == 0):
    return None
  else:
    return sum(values)




    
  