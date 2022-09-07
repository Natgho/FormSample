from rest_framework import viewsets
from .models import Consent
from .serializers import ConsentListSerializer, ConsentPostSerializer
from rest_framework import status


# Create your views here.
class ConsentViewSet(viewsets.ModelViewSet):
    queryset = Consent.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ConsentListSerializer
        elif self.action == "create":
            return ConsentPostSerializer
        return ConsentListSerializer

    def create(self, request, *args, **kwargs):
        resp = super(ConsentViewSet, self).create(request, *args, **kwargs)
        if resp.status_code == status.HTTP_201_CREATED:
            return self.list(request, *args, **kwargs)
        return resp
