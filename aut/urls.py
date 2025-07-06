from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("signup",views.signup, name='signup'),
    path("login",views.login_,name='login'),
    path("home",views.home, name='home'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
    path("aboutus",views.aboutus,name="aboutus"),
    path("faq",views.faq,name="faq"),
    path("terms",views.terms,name="terms"),
    path("contactus",views.contactus,name="contactus"),
    path("blogs",views.blogs,name="blogs"),
    path('logout',views.logout_view, name='logout'),

]