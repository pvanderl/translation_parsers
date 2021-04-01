import os

class Properties:

  def __init__(self, name = 'output'):
    name = './outputs/i18n/' + name
    try:
      os.remove(name + '.properties')
      os.remove(name + '_nl.properties')
      os.remove(name + '_fr.properties')
    except:
      pass
    self.enfile = os.open(name + '.properties', os.O_RDWR| os.O_CREAT)
    self.frfile = os.open(name + '_fr.properties', os.O_RDWR| os.O_CREAT)
    self.nlfile = os.open(name + '_nl.properties', os.O_RDWR| os.O_CREAT)

  def add_property_to_file(self, key, text, file):
    os.write(file, f'{key}={text}\n'.encode())

  def add_property(self, key, text):
    self.add_property_to_file(key, text, self.enfile)

  def add_properties(self, key, texts):
    self.add_property_to_file(key, texts[0], self.enfile)
    self.add_property_to_file(key, texts[1], self.frfile)
    self.add_property_to_file(key, texts[2], self.nlfile)
  
  def close(self):
    os.close(self.enfile)
    os.close(self.frfile)
    os.close(self.nlfile)
    
