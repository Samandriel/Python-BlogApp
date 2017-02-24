from models.post import Post
from database import Database

Database.initialize()

# post = Post(1, 'My First Blog', 'Hi this is my first blog')
#
# post.save()

posts = Post.from_blog(1)

for p in posts:
    print(p)
