import PySimpleGUI as sg

window = sg.Window("PyCon Ireland", [[]], size=(600, 600))

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
