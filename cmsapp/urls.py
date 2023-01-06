from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('member/', views.member_panel, name="member"),
    path('member/club-rules', views.club_rules, name="club-rules"),
    path('member/club-activities', views.club_activities, name="club-activities"),
    path('member/suggestion', views.suggestion, name="suggestion"),
    path('member/complain', views.complain, name="complain"),
    path('member/daily-activities', views.daily_activities, name="daily-activities"),
    path('member/specialAnnounce', views.specialAnnounce, name="specialAnnounce"),
]
