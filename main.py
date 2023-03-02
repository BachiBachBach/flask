from flask import Flask, render_template, request
import os
import geocoder
app = Flask(__name__)


@app.route('/')
def get_location():
    ip_address = request.remote_addr
    g = geocoder.ip(ip_address)
    lat = g.lat
    lng = g.lng
    return f"Your current location is ({lat}, {lng})"
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
