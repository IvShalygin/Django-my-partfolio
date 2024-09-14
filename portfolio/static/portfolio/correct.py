import PySimpleGUI as sg
import numpy as np
import pandas as pd
import os


# sg.theme("Light Blue 2")

def open_about(text_adding):
    layout = [[sg.Text(text_adding, size=(100, 20), key="new")],

              ]
    window = sg.Window("About Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break


    window.close()

l_col = sg.Column(
    [[sg.Button('Start'), sg.Cancel()]]
)
r_col = sg.Column(
    [[sg.Button("About", size=(10, 1))]],
    element_justification="right",
    vertical_alignment="bottom",
    expand_x=True,
)

# , focus=True, enable_events=True
layout = [
    [sg.Text('File input  '), sg.InputText(key='-INPUT-', focus=True, enable_events=True), sg.FileBrowse(key='-Br-'),
     ],
    [sg.Text('File output'), sg.InputText(key='-Out-'),
     ],
    [l_col, r_col],

]

window = sg.Window('Correction File by TY ', layout)

while True:  # The Event Loop
    event, values = window.read()

    if event in (None, 'Exit', 'Cancel'):

        break

    if event == '-INPUT-':
        full_name = os.path.basename(values['-INPUT-'])
        name = os.path.splitext(full_name)[0]

        name2 = os.path.dirname(values['-INPUT-']) + '/' + name + '_modify.csv'
        window['-Out-'].update(value=name2)
        values['-Out-'] = name2

    if event == 'About':
        about_txt = '''Что должна делать: 
        
v.1
На вход поступает файл из программы в формате csv кодировке UTF-8
На выходе создаем файл с такой же кодировкой и таким же форматом, но с добавлением в названии "_modify" и к столбцу 
"наименование" добавляет столбец "артикул" и добавляем наше ТУ\n
Проверок никаких не делал, подразумевается, что нужный файл подкидывается в программу в нужном виде, 
а кнопка Старт НЕ нажимается пока не введен файл'''
        open_about(about_txt)
    if event == 'Start':

        my_scv = pd.read_csv(values['-INPUT-'], delimiter=';')

        my_scv['Название'] = my_scv['Название'] + ' ' + my_scv['Внешний код'] + ' ' + 'ТУ BY 491065627.001-2022'

        my_scv.to_csv(values['-Out-'], index=False, sep=';')

window.close()
