from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from mybbs import app
from exts import db
from apps.cms import models
#3ddd

manager=Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()