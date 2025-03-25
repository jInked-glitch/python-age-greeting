def age_judge():
  age = int(input("What is your age?:   "))
  if age < 18:
      return "You are a minor."
  if 18 <= age <= 64:
      return "You are an adult."
  if age > 65:
      return "You are a senior."

def name():
  name = input("What is your name?:   ")
  return name

def greet():
  username = name()
  message = age_judge()
  return(f"Hello, {username}!\n{message}")

print(greet()) 
