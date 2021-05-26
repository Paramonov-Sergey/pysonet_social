from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/',views.FeedView.as_view(actions={'get':'retrieve'})),
    path('',views.FeedView.as_view(actions={'get':'list'})),

]
