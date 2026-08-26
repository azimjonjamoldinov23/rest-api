from django.urls import path
from . import views
from myapp.views import StudentsListAPIView , StudentsListCreateAPIView, StudentsDestroyAPIView ,StudentsRetrieveUpdateAPIView

urlpatterns = [
    path('', StudentsListAPIView.as_view(), name='home'),
    path('Students/create/',StudentsListCreateAPIView.as_view(), name='create'),
    path('Students/<int:pk>/delete/', StudentsDestroyAPIView.as_view(),name='delete'),
    path('Students/<int:pk>/update/',StudentsRetrieveUpdateAPIView.as_view(),name='update')
]