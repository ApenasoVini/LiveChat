import socketio
from django.conf import settings

sio = socketio.Server(
  cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS
)