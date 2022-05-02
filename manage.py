from app import create_app
from flask_frozen import Freezer
from flask_script import Manager,Server

app = create_app('production')
manager = Manager(app)
freezer = Freezer(app)
manager.add_command('server',Server)

@manager.command
def test():
    """
    Run unit tests.
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()