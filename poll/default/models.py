from django.db import models

# Create your models here.
class Poll(models.Model):
    subject = models.CharField("投票主題",max_length=64)
    desc=models.TextField("說明")
    created=models.DateField("建立日期",auto_now_add=True)
class Option(models.Model):
    titles = models.CharField("選項文字",max_length=64)
    votes=models.IntegerField("票數",default=0)
    pollid=models.IntegerField("投票主題編號")

    def __str__(self):
        return {"{self.pollid}-{self.titles}-{self.votes}"}