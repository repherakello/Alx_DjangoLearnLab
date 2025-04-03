from rest_framework import serializers
from tutorial.models import Tutorial, LANGUAGE_CHOICES, STYLE_CHOICES

class TutorialSerializer(serializers.serializer):
    id = serializers.IntegrField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    styles = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    # The above line is equivalent to:
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # styles = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    # The above line is equivalent to:
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # styles = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


    def create(self, validated_data):
        """
        Create and return a new `Tutorial` instance, given the validated data.
        """
        return Tutorial.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        """
        Update and return an existing `Tutorial` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.styles = validated_data.get('styles', instance.styles)
        instance.save()
        return instance