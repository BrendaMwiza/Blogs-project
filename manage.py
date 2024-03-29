from app import kora_app,db
from flask_script import Manager,Server
from app.models import Writer, Blogs, Comment, Subscription
from flask_migrate import Migrate, MigrateCommand


app = kora_app('production')
# app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Writer = Writer, Blogs = Blogs, Comment = Comment, Subscription = Subscription )


@manager.command
def test():
    """Run unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()