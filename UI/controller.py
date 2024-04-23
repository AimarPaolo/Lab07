import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        self._view.lst_result.controls.clear()
        mese_selezionato = self._view.dd_mese.value
        if mese_selezionato is None:
            self._view.create_alert("Selezionare un mese!")
            self._view.update_page()
            return
        self._view.lst_result.controls.append(ft.Text("L'umidità media nel mese selezionato è: "))
        for (chiave, valore) in self._model.get_umidita_media(mese_selezionato).items():

            self._view.lst_result.controls.append(ft.Text(f"{chiave.split("-")[1]}: {valore}"))
        self._view.update_page()



    def handle_sequenza(self, e):
        pass

    def read_mese(self, e):
        self._mese = int(e.control.value)

