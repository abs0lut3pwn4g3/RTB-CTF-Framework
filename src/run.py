import os
from FlaskRTBCTF import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG", False))
