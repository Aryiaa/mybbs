from flask import Flask

from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
import config



app=Flask(__name__)

app.config.from_object(config)
'''
使用`app.config.from_object`的方式加载配置文件：
1. 导入`import config`。
2. 使用`app.config.from_object(config)`。

使用`app.config.from_pyfile`的方式加载配置文件：
这种方式不需要`import`，直接使用`app.config.from_pyfile('config.py')`就可以了。
注意这个地方，必须要写文件的全名，后缀名不能少。
1. 这种方式，加载配置文件，不局限于只能使用`py`文件，普通的`txt`文件同样也适合。
2. 这种方式，可以传递`silent=True`，那么这个静态文件没有找到的时候，不会抛出异常。
'''


app.register_blueprint(cms_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)




@app.route
def index():
    return


if __name__=='__main__':
    app.run()