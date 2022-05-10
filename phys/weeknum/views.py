from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import InputDateForm, OutputDateForm


def get_count_weeks_year(date: date):
    """
    Функция для получения номера недели в текущем году от начала года до даты полученной функцией в качестве аргумента.
    Args:
        date (object): Объект класса date модуля datetime
    Returns:
        int: номер недели
    """
    return int(date.strftime('%U')) + 1


def get_total_count_weeks_year(year: int):
    """
    Функция для получения количества недель в году
    Args:
        year (int): год в формате yyyy
    Returns:
        int: количество недель
    """
    return int(date(year, 12, 31).strftime('%U')) + 1


def get_total_count_weeks(user_date: date, start_date: date):
    """
    Функция для получения номера недели за период от START до date
    Args:
        date (object): Объект класса date модуля datetime
    Returns:
        int: номер недели
    """
    # определяем период за который нам необходимо получить номер недели
    period = user_date.year - start_date.year
    # формируем список в котором каждый элемент это количество недель в году. Количество элементов зависит от количества полных лет в периоде.
    total_weeks = [get_total_count_weeks_year(
        start_date.year + i) for i in range(period)]
    # добавляем в список номер недели от начала года до date
    total_weeks.append(get_count_weeks_year(user_date))
    return sum(total_weeks)


class IndexView(generic.DetailView):
    template_name = 'weeknum/main.html'
    page_title = 'Программа для расчета номера недели'
    form_class = InputDateForm()

    def get(self, request, *args, **kwargs):
        form = InputDateForm()
        context = {
            'form': form,
            'page_title': self.page_title,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = InputDateForm(request.POST)
        if form.is_valid():
            template_name = 'weeknum/main_valid.html'
            user_date = form.cleaned_data['user_date']
            start_date = form.cleaned_data['start_date']
            print('User date: ', user_date)
            print('Start date: ', start_date)
            number_week = get_total_count_weeks(user_date, start_date)
            post_week = {'output_date': number_week}
            output_form = OutputDateForm(initial=post_week)
            context = {
                'form': form,
                'out_form': output_form,
                'page_title': self.page_title,
            }
            return render(request, template_name, context)

        return render(request, self.template_name, {'form': form})
