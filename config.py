import json

def get():
  f = open('config.json', 'r')
  data = json.loads(f.read())
  f.close()
  return data
