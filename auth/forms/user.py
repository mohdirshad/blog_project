from django import forms
from django.contrib.auth.models import User

#,widget=forms.TextInput(attrs={'class':'special'})
class RegistrationForm(forms.Form):
    
    #username = forms.CharField(error_messages={'required': 'please enter username .'},widget=forms.TextInput(attrs={'required':'True'}))
    email=forms.EmailField(error_messages={'required': 'please enter email Id .'},widget=forms.TextInput(attrs={'required':'True'}))
    password = forms.CharField(error_messages={'required': 'please enter password .'},widget=forms.PasswordInput(attrs={'required':'True'}))
    cpassword = forms.CharField(error_messages={'required': 'please enter confirm password .'},widget=forms.PasswordInput(attrs={'required':'True'}))
    
    
    
    first_name=forms.CharField(required=False)
    last_name=forms.CharField(required=False)
    image=forms.ImageField(required=False)

    def clean(self):
        #automatically called after calling all clean_fieldnames methods and if no one has any error
         
        cleaned_data = super(RegistrationForm, self).clean()
        if not self.errors:
            if cleaned_data.get("password")!=cleaned_data.get("cpassword"):
                raise forms.ValidationError("Both passwords must be match . ")
        return cleaned_data
    
    def clean_email(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if not self.errors:
            try:
                if User.objects.get(email=cleaned_data.get("email")):
                    raise forms.ValidationError("Email Id already registered .")
            except User.DoesNotExist:
                pass
        return cleaned_data['email']
    
#     def clean_username(self):
#         cleaned_data = super(RegistrationForm, self).clean()
#         if not self.errors:
#             try:
#                 if User.objects.get(username=cleaned_data.get("username")):
#                     raise forms.ValidationError("display name already taken, please enter different display name .")
#             except User.DoesNotExist:
#                 pass
#         return cleaned_data['username']
   

class EditRegistrationForm(forms.Form):
    #oldEmail_=None
    
    #email=forms.EmailField(error_messages={'required': 'please enter email Id .'},widget=forms.TextInput(attrs={'required':'True'}))
    first_name=forms.CharField(required=False)
    last_name=forms.CharField(required=False)
    image=forms.ImageField(required=False)
        
    def setter(self,oldEmail):
        print "in setter"
        self.oldEmail_=oldEmail

#     def clean_email(self):
#         cleaned_data = super(EditRegistrationForm, self).clean()
#         if not self.errors:
#             #print ">>",User.objects.get(email=cleaned_data.get("email")).email!=self.oldEmail_
#             try:
#                 if User.objects.get(email=cleaned_data.get("email")).email!=self.oldEmail_:
#                     raise forms.ValidationError("Email Id already registered .")
#             except User.DoesNotExist:
#                 pass
#         return cleaned_data['email']
    
# 
# f=EditRegistrationForm({'email':'imran@gmail.com'})
# print f.is_bound
# 
# print f.is_valid()
# f.setter("irfan@gmail.com")
# print f.oldEmail_
# 
#  
# print list(f.errors.values())
