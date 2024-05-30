from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form): # TODO
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class PreferencesForm(forms.Form):
    default_options = forms.MultipleChoiceField(
        choices=[
            ('文史哲藝', '文史哲藝'),
            ('法社管理', '法社管理'),
            ('理工電資', '理工電資'),
            ('生農醫衛', '生農醫衛')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    user_defined = forms.CharField(label='其他課程', max_length=100, required=False)

# class ItemForm(forms.Form):
#     main_item = forms.CharField(label='Main Item', max_length=100, initial='Main Title', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     sub_items = forms.MultipleChoiceField(
#         label='Sub Items',
#         choices=[
#             ('item1', 'Item 1'),
#             ('item2', 'Item 2'),
#             ('item3', 'Item 3'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#     custom_input = forms.CharField(label='Custom Input', max_length=100, required=False)

# class MathForm(forms.Form):
#     main_item = forms.CharField(widget=forms.HiddenInput(), initial='數學')
#     sub_items = forms.MultipleChoiceField(
#         label='',
#         choices=[
#             ('calculus', '微積分'),
#             ('linear_algebra', '線性代數'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#     custom_input = forms.CharField(label='Custom Math Input', max_length=100, required=False)

# class ChineseForm(forms.Form):
#     main_item = forms.CharField(widget=forms.HiddenInput(), initial='國文')
#     sub_items = forms.MultipleChoiceField(
#         label='',
#         choices=[
#             ('classical', '古文'),
#             ('modern', '白話文'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#     custom_input = forms.CharField(label='Custom Chinese Input', max_length=100, required=False)