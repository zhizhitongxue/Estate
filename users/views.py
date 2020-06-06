from rest_framework.generics import GenericAPIView

from users.handlers import JsonResponse
from users.serializers import IDSerializer
from users.models import UserProfile


class UserInquireView(GenericAPIView):
    serializer_class = IDSerializer

    def get(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ID = serializer.validated_data.get('ID')
            user = UserProfile.objects.get(card=ID)
            infos = {'name': user.name, 'ID': user.card, 'locate': user.locate, 'estate_num': user.estate_num,
                     'estate_card': user.estate_card, 'type': user.type, 'area': user.area, 'use': user.use,
                     'status': user.status}
            return JsonResponse(data=infos)
            # print(infos)
        else:
            raise Exception
