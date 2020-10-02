import unittest
from app.models import Comment, Blog, User
from app import db



class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Milly = User(username='Milly',password=1234)
        self.new_blog = Blog(id=1, title='Test', content='This is a test blog', user_id=self.user_Milly.id)
        self.new_comment = Comment(id=1, comment ='This is a test comment', user_id=self.user_Milly.id, blog_id = self.new_blog.id )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'This is a test comment')
        self.assertEquals(self.new_comment.user_id, self.user_charles.id)
        self.assertEquals(self.new_comment.blog_id, self.new_blog.id)

    def test_save_comment(self):
        self.new_comment.save()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comment(self):
        self.new_comment.save()
        got_comment = Comment.get_comment(1)
        self.assertTrue(get_comment is not None)