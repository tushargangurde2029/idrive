from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homepage,name='homepage' ),
    path('register',views.register,name='register' ),
    path('contactus',views.contactus,name='contactus' ),
    path('changepic',views.changepic,name='changepic' ),
    path('changepassword',views.changepassword,name='changepassword' ),
    path('profile',views.profile,name='profile' ),
    path('updateprofile',views.updateprofile,name='updateprofile' ),
    path('login',views.loginpage,name='login' ),
    path('forgot',views.forgot,name='forgot' ),
    path('logout',views.logoutuser,name='logout' ),
    path('upload',views.upload,name='upload' ),
    path('dashboard',views.dashboard,name='dashboard' ),
    path('delete/<int:id>',views.delete,name="delete"),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
