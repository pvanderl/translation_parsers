import os

class Dialog:

  def __init__(self):
    self.tabs = 0
    try:
      os.remove('./outputs/output.dialog.yaml')
    except:
        pass
    self.fs = os.open('./outputs/output.dialog.yaml', os.O_RDWR| os.O_CREAT)
    self.write_base()

  def write_file(self, text):
    os.write(self.fs, (self.tabs * '  ' + text + '\n').encode())

  def write_base(self):
    global tabs
    self.write_file('actions:')
    self.tabright()
    self.write_file('commit:')
    self.tabright()
    self.write_file('class: be.proximus.website.performance.SaveDialogActionDefinition')
    self.tableft()
    self.write_file('cancel:')
    self.tabright()
    self.write_file('class: be.proximus.website.performance.CancelDialogActionDefinition')
    self.tableft()
    self.tableft()
    self.write_file('form:')
    self.tabright()
    self.write_file('label:')
    self.write_file('tabs:')
    self.tabright()
    self.write_file('- name:')
    self.tabright()
    self.write_file('label:')
    self.write_file('fields:')

  def tabright(self):
    self.tabs += 1

  def tableft(self):
    if self.tabs > 0:
      self.tabs -= 1

  def add_field(self, key, default, i18n = True):
    label = key.split('.')[-1]
    self.write_file('- name: json.' + key)
    self.tabright()
    if i18n:
      self.write_file('i18n: true')
    self.write_file('type: String')
    self.write_file('label: ' + label)
    self.write_file('defaultValue: "' + default + '"')
    self.write_file('class: info.magnolia.ui.form.field.definition.TextFieldDefinition')
    self.tableft()