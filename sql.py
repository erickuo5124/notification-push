import sqlite3

def init():
  conn = sqlite3.connect('subscribe.db')
  print("Opened database successfully")

  conn.execute('CREATE TABLE subscribe (endpoint TEXT, p256dh TEXT, auth TEXT)')
  print("Table created successfully")
  conn.close()

def get_data():
  dbfile = "subscribe.db"
  conn = sqlite3.connect(dbfile)
  rows = conn.execute("select * from subscribe;")
  users = []
  for row in rows:
    user_info = {
      "endpoint": row[0],
      "p256dh": row[1],
      "auth": row[2]
    }
    users.append(user_info)
  conn.close()
  return users

def insert(endpoint, p256dh, auth):
  dbfile = "subscribe.db"
  conn = sqlite3.connect(dbfile)
  sql_str = "insert into subscribe(endpoint, p256dh, auth) values('{}','{}','{}');".format(endpoint, p256dh, auth)
  conn.execute(sql_str)
  conn.commit()
  conn.close()

def delete(auth):
  dbfile = "subscribe.db"
  conn = sqlite3.connect(dbfile)
  sql_str = 'DELETE FROM subscribe WHERE auth=?'
  conn.execute(sql_str, (auth,))
  conn.commit()
  conn.close()

if __name__ == '__main__':
  init()
  # subscription_info = {
  #   "endpoint":"https://fcm.googleapis.com/fcm/send/fdBNKZvXYhs:APA91bEVM02PZUs_0V8qR3Km6GBI9ID-yjhep4R8NQPvdv646UanqgH3oQFRlpw7BA_nFgkoy8SlL4sUOuwAnd_9edZT4dkR7FFoKYcjblghJ55DGGwOaCAfq-uoZ24x2l9TJZ0hpt_B",
  #   "p256dh":"BBQiPGr1HSlZ78Ytj1hjyzr9B7ERWUwZUBTTqKv3XctqiOUXa6_PWyook9qI7yblOt9IywP0OqC_lAJnsCWTjDw",
  #   "auth":"uEif1olhhAL0mJsL740pPw",
  #   "private_key" :"_8LEZ2THM7xRrzEMcez2Z3FjV_PCkHb95D0XRjav_AI"
  # }
  # insert(**subscription_info)
  # print(get_data())
  # delete('uEif1olhhAL0mJsL740pPw')