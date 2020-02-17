class Client(object):
  API_URL = 'https://example.com'

  def __init__(self, api_key=None, key_id = ""):
    self.API_KEY = api_key
    self.keyId = key_id

  def get_order_status(self, **params):
      return "Waiting..."