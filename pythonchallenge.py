import re
import pickle
import os
import tempfile
import zipfile
import requests
from bs4 import BeautifulSoup as BS, Comment

# Decorators
def challenge(*args, **kwargs):
  print("--- Challenge {} ---".format(kwargs["num"]))
  def inner(func):
    sol, url = func()
    print("Solution: {}".format(sol))
    print("Next URL: http://www.pythonchallenge.com/pc/def/{}.html\n\n".format(url if url is not None else sol))
  return inner

def main():
  # Challenges
  @challenge(num = 0)
  def chall0():
    return 2**38, None

  @challenge(num = 1)
  def chall1():
    abcd = "abcdefghijklmnopqrstuvwxyz"
    abcd2 = "cdefghijklmnopqrstuvwxyzab"
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
      # First way
    solution = ""
    i = 0
    while i < len(text):
        solution += abcd[(abcd.find(text[i])+2)%len(abcd)] if text[i] in abcd else text[i]
        i += 1
    return solution, "map".translate(text.maketrans(abcd, abcd2))

  

  @challenge(num = 2)
  def chall2():
    page = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html").text
    soup = BS(page, 'html.parser')
    text = soup.find_all(string=lambda text: isinstance(text, Comment))[1]
    return "".join(re.findall("[a-zA-Z]",text)), None

  @challenge(num = 3)
  def chall3():
    page = requests.get("http://www.pythonchallenge.com/pc/def/equality.html").text
    soup = BS(page, 'html.parser')
    text = soup.find(string=lambda text: isinstance(text, Comment))
    return "".join(re.findall(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", text)), None

  #@challenge(num = 4)
  def chall4():
    nothing = "12345"
    while nothing:
      try:
        text = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php", params={"nothing":nothing}).text
        nothing = int(re.search(r"next nothing is (\d+)", text).group(1))
      except AttributeError:
        print(text)
        if "Divide" in text:
          nothing = int(int(nothing)/2)
        else:
          return text, None

  @challenge(num = 5)
  def chall5():
    data = requests.get("http://www.pythonchallenge.com/pc/def/banner.p").text
    with open('/tmp/banner.c','w') as f:
      f.write(data)
    with open('/tmp/banner.c','rb') as f:
      data = pickle.load(f)
    
    for a in data:
      for t in a:
        print(t[0]*t[1], end='')
      print()
    
    return 'channel',None
  
  @challenge(num = 6)
  def chall6():
    star_from = "90052"
    resp = requests.get("http://www.pythonchallenge.com/pc/def/channel.zip")
    file_path = os.path.join(tempfile.gettempdir(), "channel.zip")
    folder_path = os.path.join(tempfile.gettempdir(), "channel")
    with open(file_path, 'wb') as f:
      f.write(resp.content)
    
    solution = 90052
    comments = []

    with zipfile.ZipFile(file_path, "r") as zip:
      with zip.open("readme.txt", "r") as f:
        print(f.read().decode("utf-8") )
  
      while solution:
        comments.append(zip.getinfo("{}.txt".format(solution)).comment.decode("utf-8"))
        with zip.open("{}.txt".format(solution), "r") as f:
          try:
            text = f.read().decode("utf-8") 
            solution = int(re.search(r"nothing is (\d+)", text).group(1))
          except:
            print(text, solution)
            break
    print("".join(comments))
    return "hockey",None

if __name__ == "__main__":
  main()