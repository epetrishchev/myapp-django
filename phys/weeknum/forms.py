from django import forms
from datetime import date
from django.core.exceptions import ValidationError


class InputDateForm(forms.Form):
    start_date = forms.DateField(
        label='Начало времен', initial=date(2019, 1, 1))
    user_date = forms.DateField(label='Введите дату в формате dd.mm.yyyy')

    def clean_user_date(self):
        user_date = self.cleaned_data['user_date']
        start_date = self.cleaned_data['start_date']

        if user_date < start_date:
            raise ValidationError(
                'Некорректная дата - введите дату позже 2019.01.01')

        return user_date


class OutputDateForm(forms.Form):
    output_date = forms.IntegerField(label='Номер недели: ')
