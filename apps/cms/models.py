from exts import db
from datetime import datetime

class CMSUser(db.model):
    __tablename__='cmsuser'
    id=db.Column(db.INTEGER,primary_key=True,nullable=False,autoincrement=True)
    username=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False,unique=True)
    join_time=db.Column(db.DateTime,default=datetime.now)