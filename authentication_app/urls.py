from django.urls import path
from .views import RegisterView, LoginView, DashboardView, HomeView, UserAndPetDetailsView, ListView, StartTrainingView, CompleteTrainingView

app_name = 'authentication_app'

urlpatterns=[
    path('home/', HomeView.as_view(), name = "home"),
    path('register/', RegisterView.as_view(), name = "register"),
    path('login/', LoginView.as_view(), name = "login"),
    path('dashboard/', DashboardView.as_view(), name = "dashboard"),
    path('list/', ListView.as_view(), name = "list"),
    path('userpetdetails/', UserAndPetDetailsView.as_view(), name = "userandpetdetails"),
    path('start/training/', StartTrainingView.as_view(), name = "starttraining"),
    path('complete/training/', CompleteTrainingView.as_view(), name = "completetraining"),

]