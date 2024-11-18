import socketio

from django.conf import settings
from django.utils.timezone import now

from chats.models import Chat, ChatMessage


sio = socketio.Server(
  cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS
)

@sio.event  
def update_messages_as_seen(sid, data):
    chat_id = data.get('chat_id')

    chat = Chat.objects.values(
        'from_user_id', 
        'to_user_id'
    ).filter(
        id=chat_id
    ).first()

    ChatMessage.objects.filter(
        chat_id=chat_id,
        viewed_at__isnull=True
    ).update(
        viewed_at=now()
    )

    sio.emit('update_chat', {
        'query':  {
            'users': [chat['from_user_id'], chat['to_user_id']] 
        }
    })

    sio.emit('mark_messages_as_seen', {
        'query': {
            'chat_id': chat_id,
            'exclude_user_id': data.get('exclude_user_id')
        }
    })