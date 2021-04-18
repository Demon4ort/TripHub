from django import forms

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    second_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    facebook = forms.URLField(label='Facebook')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    c_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput())
    date_of_birth = forms.DateField(label='Date of birth')
    phone = forms.CharField(label='Phone number', max_length=10)
    gender = forms.ChoiceField(label='Choose your gender', choices=GENDER_CHOICES)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        c_password = cleaned_data.get("c_password")

        if password != c_password:
            self.add_error('c_password', "Password does not match")

        return cleaned_data
