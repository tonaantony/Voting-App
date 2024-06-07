from django import forms
from .models import Candidate, Post

class VoteForm(forms.Form):
    candidate = forms.ModelChoiceField(
        queryset=Candidate.objects.none(),
        widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        post = kwargs.pop('post')
        super().__init__(*args, **kwargs)
        self.fields['candidate'].queryset = Candidate.objects.filter(post=post)
        self.fields['candidate'].widget.choices = [
            (candidate.id, candidate) for candidate in self.fields['candidate'].queryset
        ]
