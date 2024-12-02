from django.urls import path
from.views import*


urlpatterns = [
    path('all',CreatesView.as_view()),
    path('all/<int:id>',UpdateView.as_view()),
]
