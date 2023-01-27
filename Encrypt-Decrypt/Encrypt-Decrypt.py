import random

def encoding(arr):
  '''Original Message is convert into Secret Message'''
  listOfWords = arr.split(" ")
  secretMessage = ""
  for i in listOfWords :
    if len(i)<3 :
      secretMessage+= " "+i[::-1]
    else :
      startRandomWord = chr(97+random.randint(0,25)).upper() + chr(97+random.randint(0,25)) + chr(97+random.randint(0,25))
      endRandomWord = chr(97+random.randint(0,25)) + chr(97+random.randint(0,25)) + chr(97+random.randint(0,25))
      secretMessage = secretMessage + " "+ startRandomWord + i[1::]+i[0] + endRandomWord

  return secretMessage

def decoding(arr):
  '''Secret Message is convert into Original Message'''
  listOfWords = arr.split(" ")
  originalMessage = ""
  for i in listOfWords :
    if len(i)<3 :
      originalMessage+= " "+i[::-1]
    else :
      originalMessage = originalMessage + " "+ i[-4]+i[3:-4]
  return originalMessage

message = input("Enter the Message:- ")
secretMessage = encoding(message)
print("Secret Message :-"+ secretMessage)
print("Original Message :-"+ decoding(secretMessage.lstrip(" ")))

