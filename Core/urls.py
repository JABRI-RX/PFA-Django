 
from django.urls import path
from django.contrib.auth import views as auth_views
from Core.views import index,support,about,signup
from Core.forms import LoginForm
app_name = "Core"
urlpatterns = [
    path('',index,name='index'),
    path('support/',support,name='support'),
    path('about/',about,name='about'),
    path('signup/',signup,name='signup'),
# path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
