from .models import Question
from django.shortcuts import get_object_or_404
from io import StringIO 
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio   
        sys.stdout = self._stdout

def Evaluate(solution,questionid):
    question=get_object_or_404(Question.objects.all(),pk=questionid)
    user_output=solution
    score=0
    with Capturing() as user_output:
        exec(solution)
    user_output=''.join(user_output)
    if(user_output==question.sample_output):
        score=1
    return question.sample_output,user_output,score
