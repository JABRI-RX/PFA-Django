 
from django.urls import path
from Product.views import detail,new

app_name = "Product"
urlpatterns = [
     path("new/",new,name="new"),
     path("<int:pk>/",detail,name="detail")
]