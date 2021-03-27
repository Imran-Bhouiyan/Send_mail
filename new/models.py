from django.db import models


class EmailConfig(models.Model):
    email_backend = models.CharField (max_length=64, default = "django.core.mail.backends.smtp.EmailBackend")
    email_host = models.CharField (max_length = 64, default = "smtp.gmail.com")
    email_port = models.IntegerField(default = 587)
    Tls_value = models.BooleanField(default = True)
    email_host_user = models.EmailField()
    email_host_password= models.CharField(max_length = 264)
    Ssl_value = models.BooleanField(default = False)
   