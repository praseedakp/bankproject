from django import forms

# regform here
class newbankform(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    uname=forms.CharField(max_length=50)
    emailfield=forms.EmailField()
    phonenum=forms.IntegerField()
    fileimage=forms.FileField()
    pinone=forms.CharField(max_length=30)
    repin=forms.CharField(max_length=30)

# loginform here:
class newbanklogin(forms.Form):
    username=forms.CharField(max_length=50)
    newpin=forms.CharField(max_length=50)


# forms notification
class notificationform(forms.Form):
    topicnew=forms.CharField(max_length=50)
    textar=forms.CharField(max_length=50)

# forms of admin page:
class adminform(forms.Form):
    adminusername=forms.CharField(max_length=50)
    adminpassw=forms.CharField(max_length=50)


