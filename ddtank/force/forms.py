from django import forms
Loai = [('sieucao', 'sieucao'), ('3tia', '3tia')]


class HomeForm(forms.Form):
    cachban = forms.ChoiceField(label="Cach ban", choices=Loai)
    khoangcach = forms.FloatField(label="Khoang cach: ")
    docao = forms.FloatField(label="Do cao: ")
    gio = forms.FloatField(label="Gio: ")
