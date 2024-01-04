from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category_name

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')
    question_text = models.TextField()

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, db_column='question_id')
    answer_text = models.TextField()
    is_correct = models.BooleanField()

    class Meta:
        db_table = 'answers'

    def __str__(self):
        return self.answer_text

