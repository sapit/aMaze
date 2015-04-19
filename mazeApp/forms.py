from django import forms
from mazeApp.models import Maze

class ChallengeForm(forms.ModelForm):
    name = forms.CharField(widget = forms.HiddenInput)
    receivers = forms.CharField(widget=forms.Textarea, required=True)
    cells = forms.CharField(widget=forms.MultipleHiddenInput)
    width = forms.CharField(widget=forms.HiddenInput)
    height = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Maze
        fields = ['name', 'cells', 'width', 'height']