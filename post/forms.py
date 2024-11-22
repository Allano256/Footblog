from django import  forms 

from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    your_comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Type your comment here...'}),
        required=True
    )
    
        




