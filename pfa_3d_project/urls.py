 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include("Core.urls")),
    path('',include("Product.urls")),
    path('admin/', admin.site.urls),
]
