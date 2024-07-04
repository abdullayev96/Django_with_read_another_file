from django import forms
from .models import *




class FileMoveForm(forms.Form):
    file = forms.ChoiceField(label='Select a file', choices=[])
    destination = forms.CharField(label='New Path', max_length=255)

    def __init__(self, *args, **kwargs):
        file_choices = kwargs.pop('file_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['file'].choices = file_choices



class FolderForm(forms.Form):
    folder = forms.CharField(label='Folder path', max_length=255)


class FoldersForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ['path']



class FolderSelectForm(forms.Form):
    folder = forms.ModelChoiceField(queryset=DataFile.objects.all(), label="Select Folder")
    file_name = forms.CharField(label="File Name", max_length=255, required=False)