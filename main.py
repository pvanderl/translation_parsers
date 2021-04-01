import os
from properties import Properties
from dialog import Dialog


def main():
  props = Properties()
  dialog = Dialog()
  file = 'input.csv'
  fs = os.open(file, os.O_RDONLY)
  content = os.read(fs, os.path.getsize(fs))
  os.close(fs)
  for line in content.decode().splitlines()[1:]:
    l = line.split(';')
    if len([x for x in l if x != '']) == 0:
      continue
    indialog = l[1] in ['Yes', 'yes', 'y', 'Y']
    if indialog:
      dialog.add_field(l[0], l[2])
    else:
      if len(l) == 3:
        props.add_property(l[0], l[2])
      elif len(l) == 5:
        props.add_properties(l[0],)

  props.close()

main()