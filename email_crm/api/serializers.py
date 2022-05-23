from rest_framework import serializers
from email_crm.models import Email



class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        exclude = ['archived', 'read']