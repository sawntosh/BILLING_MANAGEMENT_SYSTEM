from warnings import filters
from django.shortcuts import render
from .serializers import ClientSerializer,SubscriptionPlanSerializer,SubscriptionSerializer,MetricsSerializer,HistorySerializer
from  rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework import status
from .models import *
from .models import History
# importing filters
from django_filters import rest_framework as filters
from .filters import ClientFilter,SubscriptionFilter

# Create your views here.
class ClientViewset(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

   #  def create(self, request, *args, **kwargs):
   #      serializer = self.get_serializer(data=request.data)
   #      serializer.is_valid(raise_exception=True)
   #      self.perform_create(serializer)
   #      headers = self.get_success_headers(serializer.data)
   #      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
    def destroy(self, request, *args, **kwargs):
      instance = self.get_object()
      History.objects.get_or_create(remarks=instance.name)
      self.perform_destroy(instance)
      return Response({'msg':'Delete vayo gaich'},status=HTTP_204_NO_CONTENT)

    
class SubscriptionPlanViewset(viewsets.ModelViewSet):
  queryset=SubscriptionPlan.objects.all()
  serializer_class=SubscriptionPlanSerializer

class SubscriptionViewset(viewsets.ModelViewSet):
   queryset=Subscription.objects.all()
   serializer_class=SubscriptionSerializer

class MetricsViewset(viewsets.ModelViewSet):
   queryset=Metrics.objects.all()
   serializer_class=MetricsSerializer

class HistoryViewset(viewsets.ModelViewSet):
   queryset=History.objects.all()
   serializer_class=HistorySerializer

 

#filter the result
class  ClientFilterViewset(viewsets.ModelViewSet):
   queryset=Client.objects.all()
   serializer_class=ClientSerializer
   filter_backends = [filters.DjangoFilterBackend] 
   ordering_fields=['created_at','modified_at']
   filterset_class=ClientFilter


class SubscriptionFilterViewset(viewsets.ModelViewSet):
   queryset = Subscription.objects.all()
   serializer_class = SubscriptionSerializer
   filter_backends = [filters.DjangoFilterBackend] 
   ordering_fields = ['created_at', 'modified_at']
   filterset_class = SubscriptionFilter