from flask import Flask

app = Flask(__name__)



if __name__ == "__main__":
	app.debug = True
	app.run(host= '0.0.0.0', port=5000)


from config import Config

app.config.from_object(Config)

from app import routes




#flask run --host=0.0.0.0