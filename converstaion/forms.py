from django import forms
from converstaion.models import ConvertsationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConvertsationMessage
        fields = ('content',)
        widgets = {
            'content':forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        } 