from django.shortcuts import redirect


class IsOwnerMixin:
    def is_owner(self):
        return self.object.user == self.request.user


class OwnerRequiredMixin:
    auth = None

    def get(self, request, *args, **kwargs):
        data = super().get(request, *args, **kwargs)
        if self.auth:
            if not self.object == request.user:
                return redirect('index')
            return data

        if not self.object.user == request.user:
            return redirect('index')
        return data

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        if self.auth:
            if not self.object == request.user:
                return redirect('index')
            return data

        if not self.object.user == request.user:
            return redirect('index')
        return data
