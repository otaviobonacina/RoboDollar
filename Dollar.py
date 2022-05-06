import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.google.com/search?q=dolar&sxsrf=ALiCzsYlqUtAAZtC-tVg395GlfWKzERDcw%3A1651804929688&source=hp&ei=AYt0YpfPJ5Oi1sQP9Yia8As&iflsig=AJiK0e8AAAAAYnSZEU5ozdYdXo8Dyj9xiHIGzkTeNKc_&ved=0ahUKEwjX08fw7Mn3AhUTkZUCHXWEBr4Q4dUDCAc&uact=5&oq=dolar&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIECCMQJzIKCAAQsQMQgwEQQzIECAAQQzILCAAQgAQQsQMQgwEyBAgAEEMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIECAAQQzIECAAQQzoLCC4QgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToFCAAQgAQ6BwgjELECECc6CggAELEDEIMBEAo6CwguEIAEEMcBENEDUABYwzFg3jRoAXAAeACAAXuIAb8FkgEDMC42mAEAoAEB&sclient=gws-wiz")

print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

atributos ={'class':'g'}

#respostas=soup.find_all('div',class_='g')

respostas=soup.find_all('div',attrs=atributos)

print(respostas)

