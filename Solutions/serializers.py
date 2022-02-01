from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from .models import Question,UserAnswer

class QustionListSerializer(ModelSerializer):

    class Meta:
        model=Question
        exclude=('question_id',)
    
    expand=HyperlinkedIdentityField(view_name='question-expand')
    
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request').method
        if request is not None and not request=='POST':
            [fields.pop(key) for key in ['difficulty_level','sample_input','sample_output']]
        return fields

class QuestionExpandSerializer(ModelSerializer):
    class Meta:
        model=Question
        exclude=('question_id',)
    
    answer=HyperlinkedIdentityField(view_name='question-answer')

class QuestionUpdateSerializer(ModelSerializer):

    class Meta:
        model=Question
        exclude=('question_id',)

class AnswerSerializer(ModelSerializer):

    class Meta:
        model=UserAnswer
        fields=['solution']
    
    def create(self, validated_data):
        questionid=self.context['question_id']
        instance=UserAnswer.objects.create(**validated_data)
        question=get_object_or_404(Question.objects.all(),pk=questionid)
        question.useranswer_set.add(instance)
        return instance



    


