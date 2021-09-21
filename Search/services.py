import csv

from Search.models import Post
from Search import db
from datetime import datetime


def add_posts(filename):
    with open(f'{filename}', encoding='utf-8') as csvfile:
        table = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in table:
            if count == 0:
                count += 1
                continue
            else:
                post = Post(text=row[0],
                            created_date=datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S"),
                            rubrics=row[2])
                db.session.add(post)
                db.session.commit()
            count += 1


def search(string):
    search_words = string.split(' ')
    result = []
    for post in Post.query.order_by(Post.created_date).all():
        for word in search_words:
            if str(word).lower() in str(post.text).lower():
                result.append({
                    'id': post.id,
                    'created_date': post.created_date,
                    'text': post.text,
                    'rubrics': post.rubrics
                })
    return result[:20]


def del_post(id):
    try:
        post = Post.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()
        return 'ok'
    except Exception as exc:
        return exc


if __name__ == '__main__':
    add_posts('posts.csv')
