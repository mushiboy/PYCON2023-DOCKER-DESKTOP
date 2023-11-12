import PySimpleGUI as sg


layout = [[sg.Column(
    [[
        sg.Text("Sample")
    ]], size=(300, 600)
),
    sg.Table(values=[[1, 2, 3]], headings=[
        "a", "b", "c"], size=(300, 300), expand_x=True), ]]

window = sg.Window("PyCon Ireland", layout, size=(600, 600))


while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
