from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        notification_data = [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "timestamp": n.timestamp,
                "read": n.read,
            }
            for n in notifications
        ]
        return Response(notification_data)
