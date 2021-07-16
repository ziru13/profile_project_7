import datetime

from django import forms
from django.contrib.auth.models import User

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['confirm_email',
                  'birth_date',
                  'short_bio',
                  ]

    def clean_birth_date(self):   # 要单独对这个字段进行clean才不会出现获得的value是None

        birth_date = self.cleaned_data.get('birth_date')
        date_format = '%Y-%m-%d'

        # strptime将Jul 13,2021变成纯数字格式2021-07-13，strftime将转换后的日期变成date_format这个格式
        if not datetime.datetime.strptime(str(birth_date), date_format):
            raise forms.ModelForm.ValidationError('Incorrect data format, should be YYYY-MM-DD')
        else:
            return birth_date   # 没有这个则返回None

    def clean_confirm_email(self):
        confirm_email = self.cleaned_data.get('confirm_email')
        email = self.cleaned_data.get('email')

        if confirm_email != email:
            raise forms.ModelForm.ValidationError("Emails don't match. You need to enter the same email in both fields")