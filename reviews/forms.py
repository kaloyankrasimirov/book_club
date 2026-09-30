from django import forms
from reviews.models import Review
from templates_exercise.mixins import DisabledFormMixin


# class SearchBook(forms.Form):
#     query = forms.CharField(
#         label='',
#         required=False,
#         max_length=100,
#         #TODO: add widget
#     )


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateForm(ReviewBaseForm):
    ...


class ReviewEditForm(ReviewBaseForm):
    ...

class ReviewDeleteForm(DisabledFormMixin, ReviewBaseForm):
    ...