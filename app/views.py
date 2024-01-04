from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Question
from .serializers import CategorySerializer, QuestionSerializer
import random

class CategoryQuestionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        category_id = request.data.get('category_id')
        try:
            category = Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        # Losowanie 10 unikalnych pytań z kategorii
        questions = Question.objects.filter(category=category)
        if questions.count() < 10:
            # Jeśli jest mniej niż 10 pytań, zwróć wszystkie
            selected_questions = questions
        else:
            # Losowe wybranie 10 pytań
            selected_questions = random.sample(list(questions), 10)
        
        # Utworzenie danych odpowiedzi dla wybranych pytań
        questions_data = QuestionSerializer(selected_questions, many=True).data
        return Response(questions_data)
