import re

import requests
from bs4 import BeautifulSoup


class QTCrawler:
    URL = 'http://www.365qt.com/TodaysQT.asp'

    @classmethod
    def get_html(cls):
        response = requests.get(cls.URL)
        response.encoding = None

        html = response.text

        return html

    @classmethod
    def html_to_soup(cls, html):
        html = cls.get_html()

        soup = BeautifulSoup(html, "html5lib")

        return soup

    @classmethod
    def serialize(cls):
        html = cls.get_html()
        soup = cls.html_to_soup(html)
        body = soup.find(id='content')

        parsed = dict()
        parsed['subject'] = cls._parse_subject(cls, body)
        parsed['annotation'] = cls._parse_annotation(cls, body)
        parsed['contemplation'] = cls._parse_contemplation(cls, body)
        parsed['guide'] = cls._parse_guide(cls, body)
        parsed['page'] = cls._parse_page(cls, body)
        parsed['prayer'] = cls._parse_praise(cls, body)
        parsed['word'] = cls._parse_word(cls, body)

        return parsed

    def _parse_subject(self, body):
        context = (
            body
            .select('#qtDayText2 span.qtbigText2')
            .pop()
            .get_text()
        )

        return context

    def _parse_page(self, body):
        context = (
            body
            .select('#qtDayText2 p')
            .pop()
            .get_text()
        )

        payload = (
            context.
            splitlines()[0]
            .split('(')[1]
            .replace(')', '')
        )

        book, cv = payload.split(' ')
        start, end = cv.split('~')

        # 본문말씀이 두 장으로 나누어지는 경우
        if ':' in start and ':' not in end:
            chapter, *_ = start.split(':')
            end = f'{chapter}:{end}'

        page = {
            'book': book,
            'start': start,
            'end': end
        }

        return page

    def _parse_word(self, body):
        context = (
            body
            .find('div', {'class': 'qtBox'})
            .select('li')
        )

        words = [
            re.sub(r'(<([^>]+)>)', '', (
                word.get_text()
                .replace('\xa0', '')
                .replace('\n', '')
            )) for word in context
        ]

        return words

    def _parse_annotation(self, body):
        annotations = (
            body
            .find('div', {'class': 'script'})
            .find('ul')
            .find('li')
            .select('b')
        )

        payload = list()
        for annotation in annotations:
            key, message = list(annotation.next_elements)[:2]
            payload.append(f'[ {key} ] {message}')

        return payload

    def _parse_contemplation(self, body):
        sibling = (
            body
            .find('div', {'class': 'script'})
        )

        context = (
            sibling
            .find_next_sibling('p')
        )

        # 소주제 제거
        for span in context.find_all('span'):
            span.decompose()

        # 숫자를 prefix로 가지는 문장들로 분리
        processed = re.split(r'(\d\.\s)', context.get_text())

        contemplation = list()
        for praise in processed:
            text = praise.replace('\t', '').replace('\n', '')

            if len(text) > 0:
                if text[0].isdigit():
                    contemplation.append(text)
                else:
                    contemplation[len(contemplation) - 1] += text

        return contemplation

    def _parse_guide(self, body):
        context = (
            body
            .find('div', {'class': 'bx2'})
            .find('div', {'class': 'box2Content'})
            .find('p')
        )

        return context.get_text()

    def _parse_praise(self, body):
        context = (
            body
            .find('div', {'class': 'box2'})
            .find('div', {'class': 'box2Content'})
            .select('ul li')
        )

        payload = [praise.get_text() for praise in context]

        return payload