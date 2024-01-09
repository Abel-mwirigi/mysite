from rest_framework import generics

from polls.api.serializers import QuestionSerializer, ChoiceSerializer
from polls.models import Question, Choice

class QuestionDetail(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceList(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer