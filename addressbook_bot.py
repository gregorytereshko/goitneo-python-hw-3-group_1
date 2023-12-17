from address_book import AddressBook
from record import Record
import pickle
import os

def input_error(func):
  def inner(*args, **kwargs):
      try:
          return func(*args, **kwargs)
      except ValueError:
          return "Give me name and phone please."
      except KeyError:
          return "Enter user name."
      except IndexError:
          return "Provide sufficient arguments."

  return inner

def parse_input(user_input):
  cmd, *args = user_input.split()
  cmd = cmd.strip().lower()
  return cmd, *args

@input_error
def add_contact(args, address_book):
  name, *phones = args
  record = Record(name)
  for phone in phones:
    record.add_phone(phone)
  address_book.add_record(record)

  return "Contact added."

@input_error
def change_contact(args, address_book):
  name, *phones = args
  record = address_book.find(name)
  if record is not None:
     record.update_phones(phones)

  return "Contact updated."
     
@input_error
def contact(name, address_book):
  record = address_book.find(name)
  if record is not None:
     return str(record)
  else:
     return "Record not found"

def get_contacts(address_book):
  for name, record in address_book.items():
      print(str(record))


@input_error
def add_birthday(args, address_book):
  name, birthday = args
  record = address_book.find(name)
  if record is not None:
    record.add_birthday(birthday)
    return 'Birthday added'
  else:
     return "Record not found"

@input_error
def birthday(name, address_book):
  record = address_book.find(name)
  if record is not None:
     return record.birthday.value
  else:
     return "Record not found"

def next_week_birthday(address_book):
  address_book.get_birthdays_per_week()

def dump_address_book(address_book):
  encoded_address_book = pickle.dumps(address_book)
  with open('address_book.dat', 'wb') as fh:
    fh.write(encoded_address_book)

def load_address_book():
  filename = 'address_book.dat'
  if os.path.exists(filename): 
    with open(filename, 'rb') as fh:
      encoded_address_book = fh.read()
      return pickle.loads(encoded_address_book) if encoded_address_book != '' else AddressBook()
  return AddressBook()
    

def main():
  address_book = load_address_book()
  print("Welcome to the assistant bot!")
  while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)

    if command in ["close", "exit"]:
        print("Good bye!")
        break
    elif command == "hello":
        print("How can I help you?")
    elif command == "add":
        print(add_contact(args, address_book))
    elif command == "change":
        print(change_contact(args, address_book))
    elif command == "all":
        print(get_contacts(address_book))
    elif command == "phone":
        print(contact(args[0], address_book))
    elif command == "add-birthday":
        print(add_birthday(args, address_book))
    elif command == "show-birthday":
        print(birthday(args[0], address_book))
    elif command == "birthdays":
        print(next_week_birthday(address_book))
    else:
        print("Invalid command.")
    
    dump_address_book(address_book)

if __name__ == "__main__":
  main()