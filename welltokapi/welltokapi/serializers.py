from rest_framework import serializers

from topics.models import Topic

# Serializers define the API representation.
class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('topic_id','title', 'description','author', 'tags', 'created_at', 'updated_at')