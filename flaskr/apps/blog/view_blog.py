#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from . import blog
from exts import db
from models import Article
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required
from werkzeug.exceptions import abort
from flask_login import current_user


@blog.route('/')
def index():
    articles = Article.query.order_by(Article.created_time.desc()).all()
    return render_template('blog/index.html', articles=articles)


@blog.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            article = Article(title=title, body=body, author_id=current_user.id)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@blog.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    article = get_article(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            article.title = title
            article.body = body
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', article=article)


@blog.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    article = get_article(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('blog.index'))


def get_article(id, check_author=True):
    article = Article.query.get(id)

    if article is None:
        abort(404, "Article id {0} doesn't exist.".format(id))

    if check_author and article.author_id != current_user.id:
        abort(403)

    return article
