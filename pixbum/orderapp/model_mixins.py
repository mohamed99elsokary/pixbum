from django.db.models import Sum
from django_lifecycle import (
    AFTER_CREATE,
    AFTER_UPDATE,
    BEFORE_CREATE,
    LifecycleModelMixin,
    hook,
)
from payment.models import Payment


class OrderDetailsMixin(LifecycleModelMixin):
    @hook(BEFORE_CREATE)
    def before_create(self):
        extra_cost = self.extra * self.product.extra_price
        self.price = (self.product.price * self.quantity) + extra_cost

    @hook(AFTER_CREATE)
    def after_create(self):
        from .models import Order

        order = Order.objects.filter(id=self.order_id)
        order_price = order.aggregate(total=Sum("order_details__price"))
        order = order.first()
        order.total_price = order_price["total"]
        order.save()


class OrderMixin(LifecycleModelMixin):
    @hook(AFTER_UPDATE, when="is_checkout", is_now=True)
    def payment_create(self):
        self.payment = Payment.objects.create(payment_type="ACCEPT_CREDIT_CARD")
        self.save()
