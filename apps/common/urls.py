from django.urls import path

from .views import CurrentDateView, IndexView
from .tests import RandomView

urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('random/', RandomView.as_view()),
   path('', IndexView.as_view()),
]
