from flask import Flask

app = Flask(__name__)



if __name__ == "__main__":
    app.debug = True
    app.run(host= '0.0.0.0', port=5000)


from config import Config

app.config.from_object(Config)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 2

from app import routes


@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
#flask run --host=0.0.0.0