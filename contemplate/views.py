import logging
from datetime import datetime

from django.urls import reverse
from django.shortcuts import (
    render,
    redirect
)
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


class Contemplate(View):
    def get(self, request, *args, **kwargs):
        # date 계산
        today = kwargs['date'] if 'date' in kwargs else datetime.now().strftime('%Y%m%d')
        payload = dict()

        board = None
        try:
            board = Board.objects.get(id=today)
            payload['board'] = board
        except Board.DoesNotExist:
            if self.is_sunday(today):
                return redirect(reverse('contemplate-sunday'))
            else:
                return redirect(reverse('contemplate-ready'))

        models = (
            Annotation,
            Contemplation,
            Prayer,
            Word
        )

        for model in models:
            payload[model.__name__.lower()] = (
                model
                .objects
                .filter(board_id=board.id)
                .order_by('order')
            )

        return render(request, 'contemplate.html', context=payload)

    def is_sunday(self, today: str) -> bool:
        obj = datetime.strptime(today, '%Y%m%d')
        week_number = obj.today().weekday()
        return week_number == 6


class Ready(TemplateView):
    template_name = 'ready.html'


class Sunday(TemplateView):
    template_name = 'sunday.html'
