from pywebpush import webpush, WebPushException

VAPIDKey = {
  "publicKey": "BJkRWS4HaCIjL4T0U1qemYgWm0Zjh559uqCFlDohhtM71hWpLajl423gxa_1I6klIaWjKDLfXV5R-PyPPa8I08A", 
  "privateKey": "tp5A0VlmMlUcGD_rqA08Ct52BR0SS6vIA7I32bVZtcI"
}

push_subscription = {
  "endpoint": "https://fcm.googleapis.com/fcm/send/cKTzaW2D7Hc:APA91bG8uKHhdc8_oFc_Xw2cesSYZaAuU-8qBO4hznIK9KyYXST1SVRaTU8zAE3N-cIfp8view-2--VHyP7yOBLM6Cx3uEDBOUqpRvy0SBu9CpXz7U9gSnyW42a1ypa3BBe56sV3P5FY",
  "keys": {
    "auth": "OJzIvysQOmLPZ8xxu2F_Hg",
    "p256dh": "BAgd9sHi5C7DdKejVxAZwhEQ0gFdHP2yGVwWCpN3Hwh47ncRJHfvM5JAZn8YtBYypkUm7ryivgZMaMjJMgLgky8"
  }
}

def push_notification(
  endpoint=push_subscription["endpoint"], 
  p256dh=push_subscription["keys"]["p256dh"], 
  auth=push_subscription["keys"]["auth"], 
  private_key=VAPIDKey["privateKey"],
  message=''
):
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
      data=message,
      vapid_private_key=private_key,
      vapid_claims={
        "sub": "mailto:YourNameHere@example.org",
      }
    )
    return True
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
    return False

def get_public_key():
  return VAPIDKey["publicKey"]

if __name__ == '__main__':
  push_notification()