from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Alert
from .serializers import AlertSerializer
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# class AlertViewSet(viewsets.ModelViewSet):
#     queryset = Alert.objects.all()
#     serializer_class = AlertSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def create(self, serializer):
#         serializer.save(user = self.request.user)
    
#     @action(detail=False, methods=['get'])

#     def all(self, request):
#         status = request.query_params.get('status')
#         queryset=self.filter_queryset(self.get_queryset())

#         if status:
#             queryset = queryset.filter(status=status)
        
#         page = self.paginate_queryset(queryset=queryset)
#         serializer = self.get_serializer(page, many= True)
#         return self.get_paginated_response(serializer.data)

@csrf_exempt
@login_required
def create_alert(request):
    if request.method == 'POST':
        serializer = AlertSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return JsonResponse({'message': 'Alert Created'})
        return JsonResponse({'message': 'Alert Not Created'})

@csrf_exempt
@login_required
def delete_alert(request):
    if request.method == 'DELETE':
        alert_id = request.POST.get('alert_id')
        Alert.objects.filter(id=request.POST.get('id')).delete()
        return JsonResponse({'message': 'Alert Deleted'})
    else:
        return JsonResponse({'message': 'Alert Not Deleted'})

@csrf_exempt

@login_required
def fetch_all_alerts(request):
    if request.method == 'GET':
        alerts = Alert.objects.filter(user=request.user)
        serializer = AlertSerializer(alerts, many=True)
        # add pagination
        paginator = Paginator(alerts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        response = {
            'alerts': serializer.data,
            'page_obj': page_obj,
            'has_next': page_obj.has_next(),
        }
        return JsonResponse({'alerts': serializer.data})

    else:
        return JsonResponse({'message': 'Invalid Request'})