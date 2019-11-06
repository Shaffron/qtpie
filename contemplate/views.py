import logging

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from core.models import (
    Board
)

logger = logging.getLogger(__name__)


class Contemplate(TemplateView):
    template_name = 'contemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = context.get('today')

        board = Board.objects.get(id=today)
        return context
