from rest_framework import serializers 
from . import models 
from django.contrib.auth.models import User 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__' 

class BlogPostSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(many=False) 
    class Meta:
        model = models.BlogPost 
        fields = '__all__' 
        
class DonationsSerializer(serializers.ModelSerializer):
    provide_to = serializers.StringRelatedField(many=False) 
    class Meta:
        model = models.Donations 
        fields = '__all__' 
