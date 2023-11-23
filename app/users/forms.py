from django import forms


from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['email', 'phone',]
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
    
    def clean_phone(self):
        if CustomUser.objects.filter(phone=self.cleaned_data['phone']).exists():
            return forms.ValidationError('Номер телефона уже зарегестрирован')
        return self.changed_data['phone']
    
    def clean_email(self):
        if CustomUser.objects.filter(email=self.cleaned_data['email']).exists():
            return forms.ValidationError('Такой Email уже зарегестрирован')
        return self.cleaned_data['email']
        
        
class LoginForm(forms.Form):
    phone = forms.CharField(max_length=40)
    password = forms.CharField(label='password', widget=forms.PasswordInput)