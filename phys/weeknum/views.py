from django.shortcuts import render
from django.views import generic

from .forms import InputDateForm, OutputDateForm
from .functions import get_total_count_weeks


class IndexView(generic.DetailView):
    """
    IndexView Класс представления стартовой страницы приложения
    """
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
        """
        post метод обработки запроса POST
        """
        form = InputDateForm(request.POST)
        if form.is_valid():
            # Если форма прошла валидацию, меняем шаблон страницы для рендера формы вывода номера недели
            template_name = 'weeknum/main_valid.html'
            # получаем введенную пользователем дату из формы
            user_date = form.cleaned_data['user_date']
            # получаем стартовую дату из формы
            start_date = form.cleaned_data['start_date']
            # расчитываем номер недели
            number_week = get_total_count_weeks(user_date, start_date)
            # формируем словарь для передачи в форму
            post_week = {'output_date': number_week}
            # инициализируем форму вывода номера недели с расчетным значением
            output_form = OutputDateForm(initial=post_week)
            # формируем словарь контекста для передачи в щаблон
            context = {
                'form': form,
                'out_form': output_form,
                'page_title': self.page_title,
            }
            return render(request, template_name, context)

        return render(request, self.template_name, {'form': form})
