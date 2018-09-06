from flask.blueprints import Blueprint

bp=Blueprint('front',url_prefix='/front')



@bp.route('/')
def index():
    return 'front index'