from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(label = 'Add Task', max_length = 255)

