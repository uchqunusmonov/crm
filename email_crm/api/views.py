from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .serializers import EmailSerializer
from email_crm.models import Email




class EmailList(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class GetArchivedEmails(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        emails = Email.objects.filter(user=user, archived=True)
        serializers = EmailSerializer(emails, many=True)
        return Response(serializers.data)

class GetSentEmails(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        emails = Email.objects.filter(user=user, sender =True)
        serializers = EmailSerializer(emails, many=True)
        return Response(serializers.data)

