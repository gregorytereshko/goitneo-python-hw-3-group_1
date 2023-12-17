from collections import UserDict, defaultdict
from datetime import datetime, timedelta

class AddressBook(UserDict):
  def add_record(self, record):
    self.data[record.name.value] = record

  def find(self, name):
    return self.data.get(name)

  def delete(self, name):
    if name in self.data:
      del self.data[name]

  def get_birthdays_per_week(self):
    birthdays = defaultdict(list)
    today = datetime.today().date()
    next_saturday = today + timedelta(days=-today.weekday() + 5)
    next_friday = next_saturday + timedelta(days=6)

    for name, record in self.data.items():
      birthday = record.birthday.to_datetime().date().replace(year=today.year)
      # Since we move weekend birthdays to Monday let's start our "week" from saturday
      if next_saturday <= birthday <= next_friday:
        day_of_week = birthday.strftime("%A")
        if birthday.weekday() > 4: # Saturday & Sunday check
          birthdays["Monday"].append(name)
        else:
          birthdays[day_of_week].append(name)

    for day, names in birthdays.items():
      print(f"{day}: {', '.join(names)}")