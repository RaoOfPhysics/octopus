from django.db import models
from django.urls import reverse


class Hypothesis(models.Model):
    class Meta:
        verbose_name_plural = 'hypotheses'

    text = models.TextField(blank=False)
    name = models.CharField(unique=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('hypothesis-detail', kwargs={'pk': self.pk})