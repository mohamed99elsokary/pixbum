from rest_framework import mixins


class BulkCreateModelMixin(mixins.CreateModelMixin):
    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)


class GenericCreateModelMixin(mixins.CreateModelMixin):
    def get_serializer(self, *args, **kwargs):
        if type(kwargs.get("data", {})) == list:
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)
