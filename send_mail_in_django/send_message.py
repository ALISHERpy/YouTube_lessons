# ##views.py

class SendEmailView(APIView):
    serializer_class = SendEmailSerializer
    parser_classes = (FormParser, MultiPartParser, FileUploadParser)
    permission_classes = [IsAuthenticated,]
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = serializer.validated_data.get('message')
            email = serializer.validated_data.get('email')
            try:
                send_mail(
                    subject='Test mavzu',  # Provide your subject here
                    message=f'Hello {name},\n\n{message}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
                return Response({'success': True, 'message': 'Email sent successfully'})
            except Exception as e:
                return Response({'success': False, 'message': str(e)})
        else:
            return Response({'success': False, 'message': serializer.errors})

###serializer.py:
        
class SendEmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    message = serializers.CharField()
    email = serializers.EmailField()



#### Mail in Settings.py:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = 'sizning_emailinggiz@gmail.com'
EMAIL_HOST_PASSWORD = 'app password oling'

