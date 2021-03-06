import logging

from django.db import transaction

from core.crawler import QTCrawler
from core.models import (
    Annotation,
    Board,
    Contemplation,
    Prayer,
    Word
)

logger = logging.getLogger(__name__)


@transaction.atomic
def daily_crawling():
    crawler = QTCrawler()
    payload = crawler.serialize()

    try:
        # 오늘의 큐티 게시글
        board = Board(
            subject=payload['subject'],
            paragraph=(
                f'{payload["page"]["book"]} '
                f'{payload["page"]["start"]}~{payload["page"]["end"]}'
            ),
            guide=payload['guide']
        )
        board.save()

        # 연관 데이터 저장 (말씀, 기도, 묵상항목 ...)
        _save_linked_data(board, payload)
    except Exception as e:
        logger.exception(e)

def _save_linked_data(board, payload):
    models = (
        Annotation,
        Contemplation,
        Prayer,
        Word
    )

    for model in models:
        bulk = list()
        dataset = payload[model.__name__.lower()]

        for index, message in enumerate(dataset):
            bulk.append(
                model(
                    board=board,
                    message=message,
                    order=index
                )
            )

        model.objects.bulk_create(bulk)

    return