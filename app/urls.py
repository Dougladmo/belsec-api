from app.views import ReportViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ReportViewSet)
urlpatterns = router.urls

# from django.urls import path

# urlpatterns = [
#     path('', TodoListAndCreate.as_view()),
#     path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
# ]