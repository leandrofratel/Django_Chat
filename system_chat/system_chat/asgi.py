import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system_chat.settings')

# Importe o ProtocolTypeRouter apenas depois do Django estar pronto
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

def get_websocket_application():
    # Importe as rotas DENTRO da função (após o Django estar carregado)
    from . import routing  # ← Importação tardia
    return AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": get_websocket_application(),  # ← Carrega só quando chamado
})