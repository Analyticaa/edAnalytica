from django.urls import path
from users.views import UserLoginView
from users.views import index

urlpatterns = [
      path('', index, name='index'),
      path('s/login/', UserLoginView.as_view())
]