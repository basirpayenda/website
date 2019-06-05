from django import forms
from .models import Blog
from tinymce import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class BlogForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 20, 'rows': 10}
        )
    )

    class Meta:
        model = Blog
        fields = ('title', 'category', 'content', 'overview','thumbnail', 'documents', 'featured')

