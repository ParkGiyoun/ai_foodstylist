from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import chat_message


class ChatHome(ListView):
    model = chat_message
    template_name = "chat/index.html"

    def get_context_data(self, **kwargs):
        context = super(ChatHome, self).get_context_data()
        return context



def new_chat(request, pk):
    pass