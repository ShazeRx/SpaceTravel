from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, email=None, password=None, date_of_birth=None, **extra_fields):
        if not date_of_birth:
            raise ValueError("Date of birth is required")
        return self._create_user(email=email, password=password, date_of_birth=date_of_birth,
                                 **extra_fields)

    def _create_user(self, email, password, date_of_birth=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser requires is_staff=True")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser requires is_superuser=True")
        return self._create_user(email, password, **extra_fields)
