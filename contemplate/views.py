import logging

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from core.models import (
    Annotation,
    Board,
    Bible,
    Contemplation,
    Prayer,
    Word
)

logger = logging.getLogger(__name__)


class Contemplate(TemplateView):
    template_name = 'contemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        board = Board.objects.get(id=kwargs.get('date'))
        context['board'] = board

        models = (
            Annotation,
            Contemplation,
            Prayer,
            Word
        )

        for model in models:
            key = model.__name__.lower()

            context[key] = (
                model
                .objects
                .filter(board_id=board.id)
                .order_by('order')
            )

        return context
