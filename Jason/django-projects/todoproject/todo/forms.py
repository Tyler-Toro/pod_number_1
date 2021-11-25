from django import forms


class TodoForm(forms.Form):
    task = forms.CharField(label = 'Add task', max_length = 255)

class NotesForm(forms.Form):
    notes = forms.CharField(label = 'Add notes', max_length = 500)