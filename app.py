from flask import Flask, render_template, request, redirect, url_for, jsonify
from sql import get_data, insert, delete, get_data
from push import push_notification, get_public_key
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/test')
def test():
  return 'hi'

# push notification to all subscribed user
@app.route('/push',methods = ['POST'])
def push():
  message = request.form['message']
  users = get_data()
  for user in users:
    res = push_notification(**user, message=message)
    if not res:
      delete(user['auth'])
    else:
      continue
  return redirect(url_for('home'))

# insert new user to db
# ex: curl localhost:5000/add -X POST -H "Content-Type: application/json" -d '{"endpoint":"test"}'
@app.route('/add', methods = ['POST'])
def add():
  data = request.json
  try:
    insert(
      endpoint=data['endpoint'],
      p256dh=data['keys']['p256dh'],
      auth=data['keys']['auth']
    )
    return 'success!'
  except:
    print(data)
    return 'error!'

@app.route('/show', methods = ['GET'])
def show():
  data = get_data()
  return jsonify(data)

@app.route('/key', methods=['GET'])
def get_key():
  return get_public_key()

if __name__ == '__main__':
  app.run(debug = True, port=5000)