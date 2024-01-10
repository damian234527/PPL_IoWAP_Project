from django.db import models


class Prompt(models.Model):
    question = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.TextField()
    reference = models.CharField(max_length=100)
    question = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer