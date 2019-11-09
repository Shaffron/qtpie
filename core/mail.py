import smtplib
from email.mime.text import MIMEText


'''
이거 버리고 django.core.mail 사용하기

from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)

[ settings.py 설정값들 ]
EMAIL_BACKEND
EMAIL_FILE_PATH
EMAIL_HOST
EMAIL_HOST_PASSWORD
EMAIL_HOST_USER
EMAIL_PORT
EMAIL_SSL_CERTFILE
EMAIL_SSL_KEYFILE
EMAIL_SUBJECT_PREFIX
EMAIL_TIMEOUT
EMAIL_USE_LOCALTIME
'''
class Mail:
    HOST = 'smtp.gmail.com'
    USER = 'with.alpha.and.omega'
    PASSWORD = 'llblysryeqhiunsm'
    FROM = 'Daily QT Bot'
    TO = '18vs1004@naver.com'


    @classmethod
    def get_smtp_server(self):
        smtp = smtplib.SMTP(self.HOST, 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.USER, self.PASSWORD)

        return smtp

    @classmethod
    def send_mail(cls, subject, message, to=None):
        smtp = cls.get_smtp_server()

        if not to:
            to = cls.TO

        payload = MIMEText(message)
        payload['Subject'] = subject
        payload['To'] = to

        smtp.sendmail(cls.FROM, to, payload.as_string())
        smtp.close()