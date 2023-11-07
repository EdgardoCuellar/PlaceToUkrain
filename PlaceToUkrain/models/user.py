from django.db import models

class UkrUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_host = models.BooleanField(default=False)

    @staticmethod
    def get_user_by_id(id):
        try:
            return UkrUser.objects.get(id=id)
        except:
            return False

    @staticmethod
    def get_user_by_email(email):
        try:
            return UkrUser.objects.get(email=email)
        except:
            return False
