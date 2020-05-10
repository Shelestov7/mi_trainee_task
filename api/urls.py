from django.urls import path
from .views import SecretCreateView, SecretRetrieveView


urlpatterns = [
    path('generate/', SecretCreateView.as_view()),
    path('secrets/<str:secret_key>/', SecretRetrieveView.as_view()),

]