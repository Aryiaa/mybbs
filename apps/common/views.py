from flask.blueprints import Blueprint

bp=Blueprint('common')


@bp.route('/')
def index():
    return 'common index'