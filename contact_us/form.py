


from django import forms

class ContactUsForm(forms.Form):
    name=forms.CharField(error_messages={'required':'please enter name .'},widget=forms.TextInput(attrs={'required':'True'}))
    contact_no=forms.IntegerField(required=False,error_messages={'invalid':'please enter valid contact no .'})
    email=forms.EmailField(error_messages={'required':'please enter email .'},widget=forms.TextInput(attrs={'required':'True'}))
    message=forms.CharField(error_messages={'required':'please enter message .'},widget=forms.Textarea(attrs={'required':'True','style':'height:93px'}))

    
        


#print ContactUsForm()
