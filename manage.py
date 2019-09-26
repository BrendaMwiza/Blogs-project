from app import kora_app,db
# from flask_script import Manager,Server
from app.models import User, Writer, Blog, Comment, Subscription
# from flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = kora_app('development')
# app = kora_app('production')

#Manager Commands
manager = Manager(app)
# migrate = Migrate(app,db)

#Manager Functionalities
# manager.add_command('server', Server)
# manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Writer = Writer, Blog = Blog, Comment = Comment, Subscription = Subscription )

#Testing Settings
@manager.command
def test():
    """Run unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()