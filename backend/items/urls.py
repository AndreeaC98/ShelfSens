from django.urls import path
from .views import ItemViewSet

urlpatterns = [
    path('', ItemViewSet.as_view()),
    path('<int:id>/', ItemViewSet.as_view())
]