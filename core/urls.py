from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.loginUser, name= 'login'),
    path('logout', views.logoutUser, name= 'logout'),
    path('register', views.register, name= 'register'),
    path('posting', views.posting, name= 'posting'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('edit_profile', views.update_profile, name='update_profile'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/submit_answer/', views.submit_answer, name='submit_answer'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]