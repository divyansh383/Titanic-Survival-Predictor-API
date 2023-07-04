from django.urls import path
from . import views

urlpatterns = [
    path('titanic/', views.TitanicView.as_view({'post': 'create'})),
    path('', views.index.as_view()),
]