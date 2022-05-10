from django import forms
from datetime import date
from django.core.exceptions import ValidationError


class InputDateForm(forms.Form):
    """
    InputDateForm Форма для получения даты от пользователя до которой нужно расчитать номер недели
    """
    # Стартовая дата, от которой будет начинать отсчет номера недели. Первая недели будет иметь номер 1.
    start_date = forms.DateField(
        label='Начало времен', initial=date(2019, 1, 1))
    user_date = forms.DateField(label='Введите дату в формате dd.mm.yyyy')

    def clean_user_date(self):
        # метод для проверки корректности ввода даты от пользователя. Она не должна быть раньше.ю чем стартовая дата.
        user_date = self.cleaned_data['user_date']
        start_date = self.cleaned_data['start_date']

        if user_date < start_date:
            raise ValidationError(
                'Некорректная дата - введите дату позже 2019.01.01')

        return user_date


class OutputDateForm(forms.Form):
    """
    OutputDateForm Форма для вывода расчетного значения номера недели
    """
    output_date = forms.IntegerField(label='Номер недели: ')
