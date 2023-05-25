from django.utils.crypto import get_random_string
from django_lifecycle import AFTER_CREATE, LifecycleModelMixin, hook


class UserMixin(LifecycleModelMixin):
    def soft_delete(self):
        self.is_deleted = True
        user_email = self.email
        random = get_random_string(10)
        self.email = user_email + random
        self.save()
        return self

    @hook(AFTER_CREATE)
    def create_carte(self):
        from pixbum.orderapp.models import Cart

        Cart.objects.create(user=self)
