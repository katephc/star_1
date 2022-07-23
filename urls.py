from django.urls import path
from . import views


app_name = "name_ur_app"

urlpatterns = [
    # ex: /name_ur_app/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /name_ur_app/5/
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    # ex: /name_ur_app/5/results/
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /name_ur_app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
