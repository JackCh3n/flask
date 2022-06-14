from flask import Flask, jsonify,Response, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import re,struct, sys, os, time,requests,logging
logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
