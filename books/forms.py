from django import forms

from books.models import Book, Tags
from templates_exercise.mixins import DisabledFormMixin


#
# class SearchForm(forms.Form):
#     query = forms.CharField(
#         label='',
#         required=False,
#         max_length=100,
#         #TODO: add widget
#     )
#
#

#
# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         widget=forms.Textarea(attrs={'placeholder': 'e.g. Done'})
#     )
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2
#     )
#
#     isbn = forms.CharField(
#         max_length=12
#     )

class BookBaseForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Book
        exclude = ['slug']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Insert title here'})
        }

class BookCreateForm(BookBaseForm):
    ...

class BookEditForm(BookBaseForm):
    pass


class BookDeleteForm(DisabledFormMixin, BookBaseForm):
    # class Meta(BookBaseForm.Meta):
    #     widgets = {
    #         'title': forms.TextInput(attrs={'readonly': True, 'disabled': True}), #This is to be done manually for each field.
    #     }
    ...


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
    )