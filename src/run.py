from FlaskRTBCTF import create_app
from FlaskRTBCTF.config import debugState

app = create_app()

if __name__ == '__main__':
    app.run(debug=False or debugState)