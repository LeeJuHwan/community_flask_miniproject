# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index() :
#      return render_template('index.html')


# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5002, debug=True)  
    


from .base import qna_base
import config
from flask import Flask


def create_app() :
    app = Flask(__name__)          
    app.config.from_object(config)

    from .base import main_base, board_base, login_base, qna_base
    app.register_blueprint(main_base.bp)
    app.register_blueprint(board_base.bp)
    app.register_blueprint(login_base.bp)
    app.register_blueprint(qna_base.bp)
    
    return app