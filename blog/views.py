from django.shortcuts import render
from . serializers import ProjectSerializer,BlogPostSerializer,DonationsSerializer
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import models
from datetime import datetime
# Create your views here. 

class ProjectViewset(viewsets.ModelViewSet):
    queryset = models.Projects.objects.all() 
    serializer_class =  ProjectSerializer 

class BlogPostViewset(viewsets.ModelViewSet):
    queryset = models.BlogPost.objects.all() 
    serializer_class =  BlogPostSerializer 
    

class DonationsView(APIView): 
    def post(self,request,project_id):
        try:
            amount = int(request.data.get('amount')) 
            project = models.Projects.objects.get(id = project_id)

            donation = models.Donations(provide_to =project, amount = amount) 
            donation.save()
            
            # Update the progress of the project
            project.progress += amount
            project.save()
            return Response({'message': 'Donation successful!'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    


    