from app import mail
from flask_mail import Message
from flask import current_app, render_template
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e

def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1589872509@qq.com', body='Test',
    #               recipients=['1227904039@qq.com'])
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thread = Thread(target=send_async_email, args=[app,msg])
    thread.start()
