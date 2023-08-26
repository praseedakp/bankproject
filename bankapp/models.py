from django.db import models

# Create your models here.

class newbankmodel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    uname=models.CharField(max_length=50)
    emailfield=models.EmailField()
    phonenum=models.IntegerField()
    fileimage=models.FileField(upload_to='bankapp/static')
    pinone=models.CharField(max_length=30)
    balance=models.IntegerField()
    ac_num=models.IntegerField()


#add amount models
class addamountmodel(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)


# class withdraw amount:
# withdraw model here:
class withdrawamount(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)



# model for notifications:upload by admin
class notimodel(models.Model):
    topicnew=models.CharField(max_length=50)
    textar=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)



# create a new model wishlist:user page
class wishlist(models.Model):
    uid=models.IntegerField()
    newsid=models.IntegerField()
    topicnew=models.CharField(max_length=50)
    textar=models.CharField(max_length=50)
    date=models.DateField()




# create a model for deposite and withdraw:
# class depositemodel(models.Model):
#     choice=[('Deposite','Deposite'),
#             ('Withdraw','Withdraw')
#     ]
#     select=models.IntegerField(choices=choice)
#






