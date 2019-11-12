import logging
from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from core.models import (
    Annotation,
    Board,
    Contemplation,
    Prayer,
    Word
)

logger = logging.getLogger(__name__)


class Contemplate(TemplateView):
    template_name = 'contemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # date 계산
        date = kwargs['date'] if 'date' in kwargs else datetime.now().strftime('%Y%m%d')

        board = Board.objects.get(id=date)
        context['board'] = board

        models = (
            Annotation,
            Contemplation,
            Prayer,
            Word
        )

        for model in models:
            context[model.__name__.lower()] = (
                model
                .objects
                .filter(board_id=board.id)
                .order_by('order')
            )

        logger.warning(context)

        return context
