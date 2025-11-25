from django.db import models

class ChatMessage(models.Model):
    ROLE_CHOICES = [('user', 'User'), ('model', 'AI')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Config(models.Model):
    company_name = models.CharField(max_length=100, default="Minha Empresa")
    target_audience = models.TextField(default="Geral")
    tone = models.CharField(max_length=50, default="Profissional")
    creativity = models.FloatField(default=0.7)