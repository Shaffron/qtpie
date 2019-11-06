import logging

from core.crawler import QTCrawler
from core.models import (
    Annotation,
    Board,
    Contemplation,
    Prayer,
    Word
)

logger = logging.getLogger(__name__)


def daily_crawling():
    crawler = QTCrawler()
    payload = crawler.serialize()

    try:
        # 오늘의 큐티 게시글
        board = Board(
            subject=payload['subject'],
            paragraph=(
                f'{payload["page"]["book"]} '
                f'{payload["page"]["chapter"]}장 '
                f'{payload["page"]["start"]}~{payload["page"]["end"]}절'
            ),
            guide=payload['guide']
        )
        board.save()

        # 연관 데이터 저장 (말씀, 기도, 묵상항목 ...)
        _save_linked_data(board, payload)
    except Exception as e:
        logger.exception(e)

def _save_linked_data(board, payload):
    targets = (
        ('annotations', Annotation),
        ('contemplations', Contemplation),
        ('praises', Prayer),
        ('words', Word)
    )

    for target, Model in targets:
        bulk = []
        dataset = payload[target]

        for index, message in enumerate(dataset):
            bulk.append(
                Model(
                    board=board,
                    message=message,
                    order=index
                )
            )

        Model.objects.bulk_create(bulk)

        return