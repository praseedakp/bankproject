from django.urls import path
from .views import *

urlpatterns=[
    path('frontpage/',frontfederal),
    path('newregpage1/',bankregfunction),
    path('loginone/',loginviewone),
    path('logindetails/',loginbankdetails),
    path('profilepage/',profiledesign),
    path('edithere/<int:id>',editdata),
    path('editimagepa/<int:id>',editimagepage),
    path('amountaddition/<int:id>',amountadd),
    path('paymentmethod/',paymentsucc),
    path('withdrawmethod/<int:id>',amountwithdraw),
    path('withdrawsucce/',paymentwithdraw),
    path('balancecheck/<int:id>',balancecheck),
    path('currentbala/',currentbalance),
    path('ministatementpage/<int:id>',ministatement),
    path('depodisplay/',depositeminidis),
    path('withdrawdis/',withdrawminidis),
    path('notificationpage/',notification),
    path('adminlogi/',adminlogin),
    path('adminprofilepage/',adminpropage),
    path('newsfeeddisplay/',newsdisplay),
    path('adminnewspagedisplay/',adminnewsfeed),
    path('adminnewsdelete/<int:id>',adminnewsdelete),
    path('adminnewsedit/<int:id>',adminedit),
    path('wishlist/<int:id>',wish),
    path('wishlistdisplay/',viewwishlist),
    path('logoutpage/',logout_view),
    path('wishdeleteone/<int:id>',wishremoveone),
    path('forgotpass/',forgot_password),
    path('changepinnow/<int:id>',change_password),
    path('moneytrans/<int:id>',moneytransfer)


]
