from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from .serializers import QustionListSerializer,Question,UserAnswer,AnswerSerializer,QuestionExpandSerializer,QuestionUpdateSerializer
from rest_framework.response import Response
from .utils import Evaluate
from rest_framework.views import APIView


class QuestionsListAPI(ListCreateAPIView):
    queryset=Question.objects.all()
    serializer_class=QustionListSerializer 

class QuestionExpandAPI(RetrieveAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionExpandSerializer 

class QuestionsUpdateAPI(RetrieveUpdateDestroyAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionUpdateSerializer 


class QuestionAnswerAPI(APIView):
    queryset=UserAnswer.objects.all()
    serializer_class=AnswerSerializer
    
    def post(self, request,pk):
        serializer = AnswerSerializer(data=request.data)
        serializer.context['question_id']=pk
        serializer.is_valid(raise_exception=True)
        serializer.save()
        usercode=request.data.get('solution')
        res=Evaluate(usercode,pk)
        serialized_score={'user_score':res[2],
                           'user_output':res[1],
                          'correct_output':res[0]}
        return Response(data=serialized_score)
        







        
    
        

