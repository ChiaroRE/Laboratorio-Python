class Model():

  def fit(self,data):
    raise NotImplementedError('Metodo non implementato')

  def predict(self,data):
    raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
  
  def predict(self,data):
    prev_value = None
    somma = 0
    for i in range(len(data) - 1):
      somma = somma + (data[i+1] - data[i]) 
    try:
      inc_medio = somma / (len(data) - 1)
    except((len(data) - 1) == 0):
      raise Exception('Non si può fare una predizione da un singolo elemento')
      
    prev_value = data[-1] + inc_medio
    return prev_value
      
      