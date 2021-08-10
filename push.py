from pywebpush import webpush, WebPushException

def push_notification(endpoint, p256dh, auth, private_key):
  subscription_info = {
    "endpoint": endpoint,
    "keys":{
      "p256dh": p256dh,
      "auth": auth
    }
  }

  try:
    webpush(
      subscription_info,
      data="Mary had a little lamb, with a nice mint jelly",
      vapid_private_key=private_key,
      vapid_claims={
        "sub": "mailto:YourNameHere@example.org",
      }
    )
  except WebPushException as ex:
    print("I'm sorry, Dave, but I can't do that: {}", repr(ex))
    # Mozilla returns additional information in the body of the response.
    if ex.response and ex.response.json():
      extra = ex.response.json()
      print("Remote service replied with a {}:{}, {}",
        extra.code,
        extra.errno,
        extra.message
      )