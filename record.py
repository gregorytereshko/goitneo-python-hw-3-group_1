from name import Name
from phone import Phone
from birthday import Birthday

class Record:
  def __init__(self, name):
    self.name = Name(name)
    self.phones = []
    self.birthday = None

  def add_phone(self, phone):
    self.phones.append(Phone(phone))

  def remove_phone(self, phone):
    self.phones = [p for p in self.phones if p.value != phone]

  def edit_phone(self, old_phone, new_phone):
    for phone in self.phones:
      if phone.value == old_phone:
        phone.value = new_phone
        break
  
  def update_phones(self, phones):
    self.phones = list(map(lambda phone: Phone(phone), phones))

  def find_phone(self, phone):
    for p in self.phones:
      if p.value == phone:
          return p
    return None
  
  def add_birthday(self, birthday):
    self.birthday = Birthday(birthday)

  def __str__(self):
    return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"