# app.py
import bottle
from bottle import route, template
import image

app = bottle.Bottle()

def call_service():
    directoryName = "photos"
    image.process(directoryName)

@app.route('/')
def index():
    call_service()
    return template('index.tpl', data="Request completed", title="Image Processor App")

if __name__ == "__main__":
    bottle.run(app=app, host="0.0.0.0", port=8000)
