from django.urls import path
from .views import *
from elections.views import PastElectionsView
from . import views

urlpatterns = [
    path('', RequirementsListView.as_view(), name='home'),
    # path('elections/<int:election_id>/requirements/', election_requirements, name='election_requirements'),
    path('past-elections/', PastElectionsView.as_view(), name='past_elections'),
    path('register/', register, name='register'),
    path('login/', voter_login, name='login'),
    path('dashboard/', dashboard, name='dashboard')
]