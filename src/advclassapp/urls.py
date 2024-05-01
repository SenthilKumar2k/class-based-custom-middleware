from django.urls import path
from advclassapp.views import CheckIndexView, CheckIndex

urlpatterns=[
    path('check/', CheckIndexView.as_view()),
    path('sample/', CheckIndex.as_view())
]