import logging

class Log:
  def __new__(self):
      format = '%(funcName)s-%(lineno)d : %(message)s'
      format = ''
      logging.basicConfig(encoding='utf-8', level=logging.DEBUG, format=format)
      return logging.info