from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
  path('students/',views.students_view, name="students"),
  path('students/<int:pk>/',views.student_detail, name="student_detail"),
  path('schema/', SpectacularAPIView.as_view(), name='schema'),
  path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]