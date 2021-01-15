""" routes - маршрутизация """
from flask import render_template
# render_template - рисует html-страницы
from app import app
# из файла app.py импортировать переменную app


@app.route('/')  # задать ссылку на главную страницу сайта
def main_page():  # функция отображения страницы
    return '<h1>Welcome to my site</h1>' # что будет отображаться
    """когда пользователь зайдет на главную страницу,
    он увидит текст из 10 строки"""
