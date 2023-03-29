from django import forms


class Calc_form(forms.Form):
    op = [('+', '+'), ('-', '-'), ('x', 'x'), ('/', '/')]
    first_number = forms.IntegerField()
    operation = forms.ChoiceField(choices=op, required=False)
    second_number = forms.IntegerField()
