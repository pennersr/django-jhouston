from django.db import models

class ErrorReport(models.Model):
    message = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)
    # Ideally, URLField(max_length=1024) would be used.  However,
    # MySQL has a max_length limitation of 255 for URLField.
    url = models.TextField()
    line_number = models.PositiveIntegerField()
    user_agent = models.TextField()
    remote_addr = models.IPAddressField(blank=True)
    data = models.TextField(blank=True)

    
