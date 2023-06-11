def after_payment_success(payment):
    order = payment.order
    order.status = "preparing"
    order.save()
