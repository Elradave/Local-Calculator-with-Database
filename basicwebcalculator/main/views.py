from django.shortcuts import render
from .forms import Calc_form
from . import calc
from .models import History
# Create your views here.


def home(request):
    form = Calc_form()

    if request.method == 'POST':
        first_number = int(request.POST['first_number'])
        operation = request.POST['operation']
        second_number = int(request.POST['second_number'])
        if operation == '+':
            ans = calc.add(first_number, second_number)
        elif operation == '-':
            ans = calc.subtract(first_number, second_number)
        elif operation == '/':
            ans = calc.divide(first_number, second_number)
        elif operation == 'x' or operation == '*':
            ans = calc.multiply(first_number, second_number)

        calc_history = History(first_number=first_number,
                               operation=operation, second_number=second_number, ans=ans)
        calc_history.save()

        history = History.objects.all()

        return render(request, 'main.html', {'form': form,
                                             'first_number': first_number,
                                             'operation': operation,
                                             'second_number': second_number,
                                             'ans': ans,
                                             'history': history},

                      )
    else:
        form = Calc_form()
        History.objects.all().delete()
        return render(request, 'main.html', {'form': form})
