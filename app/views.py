from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Question
from .serializers import CategorySerializer, QuestionSerializer
import random

class CategoryQuestionAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        try:
            category = Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        questions = Question.objects.filter(category=category)
        if questions.count() < 10:
            selected_questions = questions
        else:
            selected_questions = random.sample(list(questions), 10)

        questions_data = QuestionSerializer(selected_questions, many=True).data
        return Response(questions_data)
