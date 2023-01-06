
# Register your models here.
from django.contrib import admin
from .models import ClubInformation, SpecialAnnounce, ClubActivities, ClubRules, Suggestion, Complain


# Register your models here.

class SpecialAnnounceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']

admin.site.register(SpecialAnnounce)


class ClubRulesAdmin(admin.ModelAdmin):
    list_display = ('rule', 'created_on')
    search_fields = ['rule']

admin.site.register(ClubRules)


class ClubActivitiesAdmin(admin.ModelAdmin):
    list_display = ('activity_title', 'created_on')
    search_fields = ['activity_title']

admin.site.register(ClubActivities)

class ClubInformationAdmin(admin.ModelAdmin):
    list_display = ('information_title', 'created_on')
    search_fields = ['information_title']

admin.site.register(ClubInformation)

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_email')
    search_fields = ['member_name']

admin.site.register(Suggestion)

class ComplainAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_email')
    search_fields = ['member_name']

admin.site.register(Complain)


