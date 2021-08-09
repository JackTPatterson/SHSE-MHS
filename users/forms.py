from django import forms
from .models import Feedback, Announcement


GENERAL_REASON_CHOICES = [('Prospective Member', 'Prospective Member'),
                          ('Current Member', 'Current Member'),
                          ('Parent', 'Parent'),
                          ('Just Interested', 'Just Interested'),
                          ('Other', 'Other'),
                          ]


class FeedbackForm(forms.ModelForm):

    first_name = forms.CharField(required=True, label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none focus:bg-white focus:border-gray-500',

        }
    ))

    last_name = forms.CharField(label='First Name', required=False, widget=forms.TextInput(
        attrs={
            'class': 'appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none focus:bg-white focus:border-gray-500',

        }
    ))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none focus:bg-white focus:border-gray-500',


        }
    ))

    message = forms.CharField(label='First Name', required=True, widget=forms.Textarea(
        attrs={
            'class': 'no-resize appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none  focus:border-gray-500 h-48 resize-none',

        }
    ))

    person = forms.ChoiceField(required=False, choices=GENERAL_REASON_CHOICES, widget=forms.RadioSelect(
        attrs={
            'class': 'text-white mb-2',

        }
    ))

    class Meta:
        model = Feedback
        fields = ('first_name', 'last_name', 'person',
                  'email', 'message', 'person')

class AnnouncementForm(forms.ModelForm):
    
    title = forms.CharField(required=True, label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none focus:bg-white focus:border-gray-500',

        }
    ))

    message = forms.CharField(label='First Name', required=True, widget=forms.Textarea(
        attrs={
            'class': 'no-resize appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none  focus:border-gray-500 h-48 resize-none',

        }
    ))


    class Meta:
        model = Announcement
        fields = ('title', 'message')

class AnnouncementEditForm(forms.ModelForm):
    
    title = forms.CharField(required=True, label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none focus:bg-white focus:border-gray-500',
            'id': 'title'
        }
    ))

    message = forms.CharField(label='First Name', required=True, widget=forms.Textarea(
        attrs={
            'class': 'no-resize appearance-none block w-full bg-grey1 text-gray-700 rounded-lg py-3 px-4 text-white leading-tight focus:outline-none  focus:border-gray-500 h-48 resize-none',
            'id': 'message'
        }
    ))


    class Meta:
        model = Announcement
        fields = ('title', 'message')
