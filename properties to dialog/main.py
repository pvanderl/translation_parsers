import os

tabs = 0
fs = 0

def tabright():
  global tabs
  tabs += 1

def tableft():
  global tabs
  if tabs > 0:
    tabs -= 1

def add_field(name, default):
  global tabs
  write_file('- name: json.' + name)
  tabright()
  write_file('i18n: true')
  write_file('type: String')
  write_file('label: Label')
  write_file('defaultValue: "' + default + '"')
  write_file('class: info.magnolia.ui.form.field.definition.TextFieldDefinition')
  tableft()

def write_file(text):
  global tabs, fs
  os.write(fs, (tabs * '  ' + text + '\n').encode())

def write_base():
  global tabs
  write_file('actions:')
  tabright()
  write_file('commit:')
  tabright()
  write_file('class: be.proximus.website.performance.SaveDialogActionDefinition')
  tableft()
  write_file('cancel:')
  tabright()
  write_file('class: be.proximus.website.performance.CancelDialogActionDefinition')
  tableft()
  tableft()
  write_file('form:')
  tabright()
  write_file('label:')
  write_file('tabs:')
  tabright()
  write_file('- name:')
  tabright()
  write_file('label:')
  write_file('fields:')

def main():
  global fs
  file = 'input.properties'
  fs = os.open(file, os.O_RDONLY)
  content = os.read(fs, os.path.getsize(fs))
  os.close(fs)
  os.remove('dialog')
  fs = os.open('dialog', os.O_RDWR| os.O_CREAT)
  write_base()
  for line in content.decode().splitlines():
    if line[0] != '#':
      [a, b] = line.split('=')
      add_field(a, b)

main()