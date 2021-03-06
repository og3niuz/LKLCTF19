#!/usr/bin/env python3

import auth
import search
import transactions

import base64
import os
import subprocess
from collections import namedtuple
from threading import Thread

import tornado.ioloop
import tornado.web
import requests as rq
from loguru import logger



Post = namedtuple('Post', ['title', 'text', 'author'])


def smart_bot_check(html):
    logger.info('Sending request to smart_bot')

    def query():
        rq.post(os.getenv('SMART_BOT_URL'), data=html.encode('utf-8'))

    Thread(target=query, daemon=True).start()

    return ''.join([
        '<div class="w3-border w3-container w3-margin">{}</div>'.format(html),
        '<div class="w3-panel w3-padding w3-pale-green w3-text-green">',
        '    HTML-код был проверен smart_bot на безопасность',
        '</div>'
    ])


def get_posts():
    return [
        Post(
            title='У нас появился сайт!',
            text=(
                'Приветствуем вас на нашем сайте! Мы создали его достаточно недавно, и он нам нужен, чтобы '
                'повысить качество обслуживания клиентов. Мы использовали только проверенные и безопасные '
                'технологии, так что вероятность взлома сайта или аккаунтов какого-то из пользователей '
                'сведена к минимуму. Надеемся, вам будет приятно пользоваться нашим сайтом'
            ),
            author='user1',
        ),
        Post(
            title='Логотип банка',
            text=(
                '<img src="/static/image1.png" height=300 alt="image"></img>'
                '<!-- static/image-512df359789cee50e97f40d25272c0b84d94459bc8631ce32132a5942f022d77.png -->'
            ),
            author='admin',
        ),
        Post(
            title='Тестовая запись',
            text='Текст тестовой записи',
            author='smart_bot',
        ),
    ]


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return auth.maybe_get_user_by_session(self.get_cookie('session_id'))


class HomepageHandler(BaseHandler):
    def get(self):
        self.render('templates/index.html', posts=get_posts())


class InfoHandler(BaseHandler):
    def get(self):
        self.redirect('/static/code-15f4996b5aad4ced417d4bd9d58e2c62.tar.gz')


class SignInHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', '')
        otp = self.get_argument('otp', None)
        password_hash = auth.hash_password(password)
        session_id = auth.maybe_authorize_user(username, password_hash, otp)
        if session_id is None:
            self.render('templates/bad-auth.html')
        else:
            logger.info('User {} logged in, session_id = {}', username, session_id)
            self.set_cookie('session_id', session_id)
            self.redirect('/')


class ViewUserInfoHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', '')
        password_hash = auth.hash_password(password)
        user = auth.maybe_get_user_by_full_creds(username, password_hash)
        if user is None:
            self.render('templates/bad-auth.html')
        else:
            self.render('templates/view-user-info.html', user=user)


class SelfHandler(BaseHandler):
    def get(self):
        if self.current_user is None:
            self.redirect('/sign-in-form')
            return
        transactions_info = transactions.get_transactions(self.current_user)
        self.render('templates/self.html', transactions=transactions_info)


class SearchHandler(BaseHandler):
    def get(self):
        if self.current_user is None:
            self.redirect('/sign-in-form')
            return
        query = self.get_argument('query', '')
        html = search.search(query)
        checked_html = smart_bot_check(html)
        self.write(checked_html)


class LogOutHandler(BaseHandler):
    def get(self):
        session_id = self.get_cookie('session_id')
        self.clear_cookie('session_id')
        self.redirect('/')


class SimpleHandler(BaseHandler):
    def initialize(self, filename):
        self.filename = filename

    def get(self):
        self.render(self.filename)


def main():
    port = int(os.getenv('SERVICE_PORT', 9999))
    app = tornado.web.Application(
        [
            ('/', HomepageHandler),
            ('/info', InfoHandler),
            ('/log-out', LogOutHandler),
            ('/search', SearchHandler),
            ('/self', SelfHandler),
            ('/sign-in', SignInHandler),
            ('/sign-in-form', SimpleHandler, {'filename': 'templates/sign-in-form.html'}),
            ('/view-user-info', ViewUserInfoHandler),
            ('/static/(.*)', tornado.web.StaticFileHandler, {'path': './static'}),
        ],
        debug=False,
        autoreload=False,
    )
    app.listen(port)
    logger.info('Server started on port {}', port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
