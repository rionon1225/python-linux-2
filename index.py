import bottle
from bottle import template
import image

app = bottle.Bottle()

def call_service():
    directoryName = "photos"
    image.process(directoryName)

@app.route("/")
def index():
    call_service()
    return template("index.tpl", data="Request completed", title="Image Processor App")
