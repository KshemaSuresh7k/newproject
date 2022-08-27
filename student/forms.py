from django import forms
from .models import studreg,parreg,eventadd,leave

class registerform(forms.ModelForm):
    class Meta:
        model=studreg
        fields=('sname','admno','department','year','course','email','password','contactno')
        widgets={
            'sname':forms.TextInput(attrs={'class':'form-contol'}),
            'admno':forms.TextInput(attrs={'class':'form-contol'}),
            'department':forms.TextInput(attrs={'class':'form-contol'}),
            'year':forms.TextInput(attrs={'class':'form-contol'}),
            'course':forms.TextInput(attrs={'class':'form-contol'}),
            'email':forms.TextInput(attrs={'class':'form-contol'}),
            'password':forms.TextInput(attrs={'class':'form-contol'}),
            'contactno':forms.TextInput(attrs={'class':'form-contol'}),
        }


class parentform(forms.ModelForm):
    class Meta:
        model=parreg
        fields=('username','sid','department','sname','email','password','contactno')
        Widgets={
            'username':forms.TextInput(attrs={'class':'form-contol'}),
            'sid':forms.TextInput(attrs={'class':'form-contol'}),
            'department':forms.TextInput(attrs={'class':'form-contol'}),
            'sname':forms.TextInput(attrs={'class':'form-contol'}),
            'email':forms.TextInput(attrs={'class':'form-contol'}),
            'password':forms.TextInput(attrs={'class':'form-contol'}),
            'contactno':forms.TextInput(attrs={'class':'form-contol'}),
        }



class eventaddform(forms.ModelForm):
    class Meta:
        model=eventadd
        fields=('eventname','department','date','day','time')
        widgets={
            'eventname':forms.TextInput(attrs={'class':'form-contol'}),
            'department':forms.TextInput(attrs={'class':'form-contol'}),
            'date':forms.TextInput(attrs={'class':'form-contol'}),
            'day':forms.TextInput(attrs={'class':'form-contol'}),
            'time':forms.TextInput(attrs={'class':'form-contol'}),
        }

class leaveform(forms.ModelForm):
    class Meta:
        model=leave
        fields=('name','admno','date','days','reason','status')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-contol'}),
            'admno':forms.TextInput(attrs={'class':'form-contol'}),
            'date':forms.TextInput(attrs={'class':'form-contol'}),
            'days':forms.TextInput(attrs={'class':'form-contol'}),
            'reason':forms.TextInput(attrs={'class':'form-contol'}),
            'status':forms.TextInput(attrs={'class':'form-contol'}),
        }

