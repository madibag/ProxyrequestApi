from flask import Flask, request
import proxygrabber

app = Flask(__name__)
app.secret_key = 'test'
app.url_map.strict_slashes = False

@app.route('/')
def home():
   return "Proxy is up!"

@app.route('/proxy/', methods=['GET'])
def result():
    return send_from_directory('','proxy.json')


@app.route('/surf/result/',methods=['GET'])
def download():
    query = request.args.get('url')
    proxygrabber.make_request(query)
    return co


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
