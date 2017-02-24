import uuid
import datetime
from database import Database

class Post:

    def __init__(self, blog_id, title, content, author="Harris", date=datetime.datetime.utcnow(), id=None):    # id is optional
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id     # Generate random number if id not defined
        self.title = title
        self.content = content
        self.created_date = date
        self.author = author

    def save(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one('posts', {'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blog_id': id})]