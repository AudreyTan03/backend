from rest_framework import serializers
from .models import *


class AdminVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class UploadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        user = request.user if request else None
        
        # If a user is authenticated and has a valid subscription for the associated product, allow access
        if request.user and instance.is_accessible(user):
            return data
        else:
            # Nakasub dapat user para maaccess
            data['message'] = "You must be subscribed to access this video." 
            return data   


class DeleteVideoSerializer(serializers.Serializer):
    video_id = serializers.IntegerField()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

