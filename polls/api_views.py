from rest_framework import viewsets
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

class QuestionPaginator(PageNumberPagination):
    page_size = 5

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,AllowAny]
    pagination_class=QuestionPaginator


# class ChoiceViewSet(viewsets.ModelViewSet):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly,AllowAny]

class   ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,AllowAny]

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.request.data.get('question_id'))
        serializer.save(question=question)

