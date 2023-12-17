import re
from datetime import datetime

from field import Field

class Birthday(Field):
  def __init__(self, value):
    if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', value):
      raise ValueError("Birthday must be DD.MM.YYYY format")
    super().__init__(value)
  
  
  def to_datetime(self):
    return datetime.strptime(self.value, "%d.%m.%Y")