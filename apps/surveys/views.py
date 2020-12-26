from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.surveys.serializers import SurveySerializer, QuestionSerializer, AnswerSerializer
from apps.surveys.models import Survey, Question, Answer

def listToString(s):  
    # return string   
    return ','.join([str(elem) for elem in s]) 

class SurveyAPIView(APIView):
    def get(self, request, pk=None):
        surveys = Survey.objects.all()
        surveys_serializer = SurveySerializer(surveys, many=True)
        return Response(surveys_serializer.data, status=status.HTTP_200_OK)

class SurveyDetailAPIView(APIView):
    def get(self, request, pk=None):
        survey = Survey.objects.filter(id=pk).first()
        survey_serializer = SurveySerializer(survey)
        return Response(survey_serializer.data, status=status.HTTP_200_OK)

class QuestionAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        questions_serializer = QuestionSerializer(questions, many=True)
        return Response(questions_serializer.data, status=status.HTTP_200_OK)

class AnswerAPIView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        answers_serializer = AnswerSerializer(answers, many=True)
        return Response(answers_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        #return Response(request.data)
        for answer in request.data:
            if answer['options']:
                answer['options'] = listToString(answer['options'])
            asnwer_serializer = AnswerSerializer(data=answer)
            if asnwer_serializer.is_valid():
                asnwer_serializer.save()
        return Response({'message', 'La encuesta ha sido registrada correctamente.'}, status=status.HTTP_200_OK)