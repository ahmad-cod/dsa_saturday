# Use Cases
# 1. Mapping or modeling a relationship from one item to another
phone_book = {}
phone_book["Adam"] = "09012345678"
phone_book["Musa"] = "08012345679"
print(phone_book["Adam"])

# 2. Filtering out Duplicate
voted = {}
def check_voter(name):
  if name in voted:
    print(f"{name} already voted, Kick them out!")
  else:
    voted[name] = True
    print("Let them vote!")

check_voter("Adam")
check_voter("Musa")
check_voter("Musa")

# 3. Caching or memoizing data, instead of making server do work

cache = {}

def get_data_from_server(url):
  # Just a Pseudocode
  pass

def get_url(url):
  if url in cache:
    return cache[url]
  else:
    data = get_data_from_server(url)
    cache[url] = data
    return data