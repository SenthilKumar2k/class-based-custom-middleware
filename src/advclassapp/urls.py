from django.urls import path
from advclassapp.views import CheckIndexView

urlpatterns=[
    path('check/', CheckIndexView.as_view())
]