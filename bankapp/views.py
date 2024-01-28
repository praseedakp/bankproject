from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout


# Create your views here.
def frontfederal(request):
    return render(request,'frontpagefederal.html')

#registration function
def bankregfunction(request):
    if request.method=='POST':
        a=newbankform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            un=a.cleaned_data['uname']
            em=a.cleaned_data['emailfield']
            pho=a.cleaned_data['phonenum']
            fi=a.cleaned_data['fileimage']
            pn=a.cleaned_data['pinone']
            cp=a.cleaned_data['repin']
            ac=int('15'+str(pho))
            if pn==cp:
                b=newbankmodel(fname=fn,lname=ln,uname=un,emailfield=em,phonenum=pho,fileimage=fi,pinone=pn,balance=0,ac_num=ac)
                b.save()
                subject="your account has been created"
                message=f"your new account number is {ac}"
                email_from="ctpraseeda8064@gmail.com"
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return redirect(loginbankdetails)
            else:
                return HttpResponse("pin does not match !!!")
        else:
            return HttpResponse("registration failed")
    return render(request,'indexone.html')

# login to seen:
def loginviewone(request):
    return render(request,'loginpage.html')

# login code:
def loginbankdetails(request):
    if request.method=='POST':
        s=newbanklogin(request.POST)
        if s.is_valid():
            ue=s.cleaned_data['username']
            pm=s.cleaned_data['newpin']
            r=newbankmodel.objects.all()
            for i in r:
                if i.uname==ue and i.pinone==pm:
                    request.session['id']=i.id
                    return redirect(profiledesign)
            else:
                return HttpResponse("login failed!!!")
    return render(request,'loginpage.html')

# profile page display:
def profiledesign(request):
    try:
        id1=request.session['id']
        a=newbankmodel.objects.get(id=id1)
        img=str(a.fileimage).split('/')[-1]
        return render(request,'profilepage.html',{'a':a,'img':img})
    except:
        return redirect(loginbankdetails)

# edit the data
def editdata(request,id):
    a=newbankmodel.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('finame')
        a.lname=request.POST.get('laname')
        a.emailfield=request.POST.get('emailf')
        a.phonenum=request.POST.get('pho')
        a.save()
        return redirect(profiledesign)
    return render(request,'editdetailspage.html',{'a':a})



# image edit:
def editimagepage(request,id):
    a=newbankmodel.objects.get(id=id)
    img=str(a.fileimage).split('/')[-1]
    if request.method=='POST':
        a.uname=request.POST.get('upacc')
        if len(request.FILES)!=0:
            if len(a.fileimage)>0:
                os.remove(a.fileimage.path)
            a.fileimage=request.FILES['upfile']
        a.save()
        return redirect(profiledesign)
    return render(request,'profilepicedit.html',{'a':a,'img':img})


# deposit function:
def amountadd(request,id):
    x=newbankmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        request.session['am']=am
        request.session['ac_num']=x.ac_num
        pin = request.POST.get('pinold')
        if pin == x.pinone:
            x.balance+=int(am)
            x.save()
            b=addamountmodel(amount=am,uid=request.session['id'])
            b.save()
            return redirect(paymentsucc)
        else:
            return HttpResponse('amount added failed!!!')
    return render(request,'amountpage.html')


# payment adding function:
def paymentsucc(request):
    am=request.session['am']
    acc=request.session['ac_num']
    return render(request,'paymentsuccess.html',{'am':am,'acc':acc})


#withdraw amount using balance and pin:
def amountwithdraw(request,id):
    k=newbankmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amountwi')
        request.session['am']=am
        request.session['ac_num']=k.ac_num
        if k.balance>int(am):
            k.balance-=int(am)
            k.save()
            c=withdrawamount(amount=am,uid=request.session['id'])
            c.save()
            pin=request.POST.get('pinwi')
            if pin==k.pinone:
                return redirect(paymentwithdraw)
            else:
                return HttpResponse('withdraw failed!!!')
    return render(request,'withdrawpage.html')


# payment withdraw page:
def paymentwithdraw(request):
    amt=request.session['am']
    acco=request.session['ac_num']
    return render(request,'paymentwithdrawsucce.html',{'amt':amt,'acco':acco})



# check balance:
def balancecheck(request,id):
    k=newbankmodel.objects.get(id=id)
    if request.method=='POST':
        pin=request.POST.get('pinb')
        request.session['balance']=k.balance
        request.session['ac_num']=k.ac_num
        if pin==k.pinone:
            return redirect(currentbalance)
        else:
            return HttpResponse("balance check failed")

    return render(request,'balancecheck.html')



# balace success:
def currentbalance(request):
    a=request.session['balance']
    ac=request.session['ac_num']
    return render(request,'balanceshow.html',{'ac':ac,'a':a})





# ministatement with dropdown:
def ministatement(request,id):
    a=newbankmodel.objects.get(id=id)
    pin=request.POST.get('minipin')
    if request.method=='POST':
        if pin==a.pinone:
            choice=request.POST.get('select')
            if choice=="Deposite":
                return redirect(depositeminidis)
            elif choice=="Withdraw":
                return redirect(withdrawminidis)
        else:
            return HttpResponse("password error!!!")

    return render(request,'showministatement.html')



# deposite display:
# take the id of login member then pass to frontend for display

def depositeminidis(request):
    x=addamountmodel.objects.all()
    id=request.session['id']
    return render(request,'depositeministmtdisplay.html',{'x':x,'id':id})



# withdraw ministatement display:
def withdrawminidis(request):
    y=withdrawamount.objects.all()
    id=request.session['id']
    return render(request,'withdrawminidisplay.html',{'y':y,'id':id})


# newsfeed .......

def notification(request):
    if request.method=='POST':
        m=notificationform(request.POST)
        if m.is_valid():
            to=m.cleaned_data['topicnew']
            con=m.cleaned_data['textar']
            b=notimodel(topicnew=to,textar=con)
            b.save()
            return redirect(adminnewsfeed)
        else:
            return HttpResponse("News Feed Failed")
    return render(request,'newsfeed.html')

# admin login page:
def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['adminusername']
            password=a.cleaned_data['adminpassw']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return redirect(adminpropage)

            else:
                return HttpResponse("Login failed")

    return render(request,'adminloginpage.html')


# adminprofilepage:
# 2 button :add newsfeed,display newsfeed
def adminpropage(request):
    return render(request,'adminprofilepage.html')

#user newsfeed display:
# search box implemented:button is given
# button from profile page:
# heart symbol:wishlist add cheyyum..item undengil already added message printed
# wishlistdisplay is html page

def newsdisplay(request):
    s=notimodel.objects.all()
    return render(request,'newsfeeddisplaypage.html',{'s':s})

# admin newsfeed display:edit and delete button
def adminnewsfeed(request):
    k=notimodel.objects.all()
    return render(request,'adminnewsfeeddisplay.html',{'k':k})

# delete the content by admin:
def adminnewsdelete(request,id):
    a=notimodel.objects.get(id=id)
    a.delete()
    return redirect(adminnewsfeed)

# edit the newsfeeddata admin:
def adminedit(request,id):
    a=notimodel.objects.get(id=id)
    if request.method=='POST':
        if request.POST.get('topnewedit')=='':
            a.save()
        else:
            a.textar=request.POST.get('contentedit')
        a.topicnew=request.POST.get('topnewedit')
        a.save()
        return redirect(adminnewsfeed)
    return render(request,'adminnewseditpage.html',{'a':a})

# deposite and withdraw by one person display:
# print by js:
# search box implementation in user display html:js


# wishlist model create and button in newsfeeddisplay.html:
# to add to wishlist and if items already in wishlist it print msg
# item is added by uid :so we get particular person wishlist only.
def wish(request,id):
    a=notimodel.objects.get(id=id)
    wish=wishlist.objects.all()
    for i in wish:
        if i.newsid==a.id and i.uid==request.session['id']:
            return HttpResponse("item already in wishlist...")
    b=wishlist(topicnew=a.topicnew,textar=a.textar,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return HttpResponse("added to wishlist")


# wishlist display:new html page for display
def viewwishlist(request):
    b=wishlist.objects.all()
    id=request.session['id']
    return render(request,'wishlistdisplay.html',{'b':b,'id':id})


# remove newsfeed from wishlist:
def wishremoveone(request,id):
    a=wishlist.objects.get(id=id)
    if a.uid==request.session['id']:
            a.delete()
    return redirect(viewwishlist)


# logout:after login the page want to logout use this function
def logout_view(request):
    logout(request)
    return redirect(loginbankdetails)

# forgot password:views
def forgot_password(request):
    a=newbankmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('emailfield')
        ac=request.POST.get('ac_num')
        for i in a:
            if (i.emailfield==em and i.ac_num==int(ac)):
                id=i.id
                subject="please change your pin......."
                message=f"http://127.0.0.1:8000/bankapp/changepinnow/{id}"
                frm="ctpraseeda8064@gmail.com"
                to=em
                send_mail(subject,message,frm,[to],ac)
                return HttpResponse("check mail")
        else:
            return HttpResponse("sorry...")
    return render(request,'forgotpage.html')


# pinchange views:
def change_password(request,id):
    a=newbankmodel.objects.get(id=id)
    if request.method=='POST':
        # htmlpage pin:changepin here
        pi=request.POST.get('pinone')
        repi=request.POST.get('repin')
        if pi==repi:
            a.pinone=pi
            a.save()
            return HttpResponse("password changed successfully.....Thankyou")
        else:
            return HttpResponse("sorry....Some error occured...please check again...")
    return render(request,'changepin.html')
# int id venam urls of changepassword:





# money transfer views:
# account:holeder:amal
# accountnumber:ayalde account:300 avanam(increment)
# ayakkunna alde balance:-decrement

# b:moneytranfer person te mode:
# a:login cheyth kittana person

def moneytransfer(request,id):
    a=newbankmodel.objects.get(id=id)
    b=newbankmodel.objects.all()
    if request.method=='POST':
        n=request.POST.get('holdername')
        m=request.POST.get('acnumber')
        k=request.POST.get('amount')
        for i in b:
            if n==i.fname and int(m)==i.ac_num:
                if a.balance>=int(k):
                    a.balance -= int(k)
                    i.balance+=int(k)
                    i.save()
                    a.save()
                    return HttpResponse("Money transfered successfully...")
                else:
                    return HttpResponse("sorry...insufficient balance...")
        else:
            return HttpResponse("user not found..")
    return render(request,'moneytransfer.html')

