from pypdf import PdfReader
import flet as fl
def main(page:fl.Page):
    def clear(e):
        column.controls = []
        b_clear.disabled=True
        page.update()
    def pdf(e:fl.FilePickerResultEvent):
        clear(e)
        text=PdfReader(e.files[0].name)
        for n in range(len(text.pages)):
            column.controls.append(fl.Text('PAGE '+str(n+1)+'\n\n'+text.pages[n].extract_text()))
            b_clear.disabled=False
        page.update()
    picker=fl.FilePicker(on_result=pdf)
    page.overlay.append(picker)
    b_clear=fl.ElevatedButton('CLEAR',disabled=True,on_click=clear)
    column=fl.Column(scroll=fl.ScrollMode.ALWAYS,height=500)
    page.add(fl.Row(controls=[fl.ElevatedButton('SELECT PDF',icon=fl.icons.UPLOAD_FILE,on_click=lambda _:picker.pick_files(allow_multiple=False)),
                              b_clear,
                              fl.IconButton(icon=fl.icons.EXIT_TO_APP_OUTLINED,icon_color='red',icon_size=30,on_click=lambda _:page.window_destroy())]),
             column)
fl.app(target=main)
