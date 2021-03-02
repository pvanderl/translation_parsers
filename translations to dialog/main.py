import os
import json

tabs = 0
fs = 0


def tabright():
    global tabs
    tabs += 1


def tableft():
    global tabs
    if tabs > 0:
        tabs -= 1


def add_field(name, defaultValue):
    global tabs
    label = name.split('.')[-1]
    write_file('- name: json.' + name)
    tabright()
    write_file('i18n: true')
    write_file('type: String')
    write_file('label: ' + label)
    write_file('defaultValue: "' + defaultValue + '"')
    write_file(
        'class: info.magnolia.ui.form.field.definition.TextFieldDefinition')
    tableft()


def add_tab(name):
    global tabs
    write_file('- name: ' + name)
    tabright()
    write_file('label:')
    write_file('fields:')
    tabright()


def write_file(text):
    global tabs, fs
    os.write(fs, (tabs * '  ' + text + '\n').encode())


def write_base():
    global tabs
    write_file('actions:')
    tabright()
    write_file('commit:')
    tabright()
    write_file(
        'class: info.magnolia.ui.admincentral.dialog.action.SaveDialogActionDefinition'
    )
    tableft()
    write_file('cancel:')
    tabright()
    write_file(
        'class: info.magnolia.ui.admincentral.dialog.action.CancelDialogActionDefinition'
    )
    tableft()
    tableft()
    write_file('form:')
    tabright()
    write_file('label:')
    write_file('tabs:')
    tabright()


def main():
    global fs
    with open('input.translations') as file:
        data = json.load(file)
        os.remove('dialog')
        fs = os.open('dialog', os.O_RDWR | os.O_CREAT)
        write_base()
        for a in data.keys():
            if a[0] != '#' and not 'generic' in a:
                add_field(a, data[a])
            elif a == '#tab':
                add_tab(data[a])


main()
