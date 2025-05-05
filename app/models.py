from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from bson.objectid import ObjectId  # Required for MongoDB ObjectId

# Project Model
class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.start_date:
            self.week_number = str(self.start_date.isocalendar()[1])  # Ensure it's a string
        super().save(*args, **kwargs)

# Custom User Model
class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=24, default=str(ObjectId()), editable=False)  # Set ObjectId as primary key
    email = models.EmailField(unique=True)  # ✅ Added Email Field
    otp_secret = models.CharField(max_length=16, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        through='UserGroup'  # Explicit intermediate model
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        through='UserPermission'  # Explicit intermediate model
    )

    class Meta:
        db_table = "users"  # ✅ Change collection name from `app_user` to `users`

# Many-to-Many Relationship Models
class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)