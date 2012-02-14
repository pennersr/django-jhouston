from django.db import models

class ErrorReport(models.Model):
    message = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=255)
    line_number = models.PositiveIntegerField()
    user_agent = models.CharField(max_length=255)
    remote_addr = models.IPAddressField(blank=True)
    data = models.TextField(blank=True)

    
