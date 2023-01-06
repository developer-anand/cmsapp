from django.db import models

# Create your models here.




# Create your models here.
class SpecialAnnounce(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class ClubRules(models.Model):
    rule = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']



class ClubActivities(models.Model):

    activity_title = models.CharField(max_length=100,unique=True)
    activity_desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.activity_title

class ClubInformation(models.Model):
    information_title = models.CharField(max_length=100,unique=True)
    information_desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.information_title

class Suggestion(models.Model):
    member_name = models.CharField(max_length=100)
    member_email = models.EmailField()
    member_suggestion = models.TextField()

    def __str__(self):
        return self.member_name

class Complain(models.Model):
    member_name = models.CharField(max_length=100)
    member_email = models.EmailField()
    member_complain = models.TextField()

    def __str__(self):
        return self.member_name