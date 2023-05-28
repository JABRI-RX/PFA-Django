from django.urls import path

from converstaion.views  import new_conversation,inbox

app_name = 'conversation'

urlpatterns = [
    path("",inbox,name="inbox"),
    path("new/<int:item_pk>/",new_conversation,name="new"),
]


