from flask import Flask, jsonify,Response, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import re,struct, sys, os, time,requests,logging
logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

app = Flask(__name__)

if os.environ.get("TOKEN"):
    updater = Updater(os.environ.get("TOKEN"), use_context=True)
else:
    REQUEST_KWARGS={
        'proxy_url': 'http://127.0.0.1:10809',
    }
    updater = Updater('', use_context=True, request_kwargs=REQUEST_KWARGS)
# 首页
@app.route('/')
def index():
    return jsonify({'code':200,'msg':'hello word'})

# 推送
@app.route('/u/<path:users>/t/<path:texts>', methods=['POST'])
def message_push(texts,users):
    if not texts and not users:
        return jsonify({'code':404,'msg':'not find'})
    print(texts,users)
    updater.bot.send_message(text=texts, chat_id=users)
    return jsonify({'code':200})

# ip
@app.route('/ip', methods=['GET'])
def ip():
    return Response(request.remote_addr, mimetype="text/text")

# 404
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'code':404,'msg':'not find'})

if __name__ == '__main__':
    print('PORT',os.getenv("PORT",default=5000))
    print('PORT',os.environ.get("PORT"))
    app.run(debug=True, port=os.getenv("PORT", default=5000))
