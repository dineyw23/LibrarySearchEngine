#SearchEngine
from Media import Media
from Book import Book
from Periodical import Periodical
from Video import Video
from Film import Film

class SearchEngine(Media):
  global CardCatalog
  CardCatalog = list()
  def __init__ (self):
    inf = open('book.txt','r')
    if inf.closed:
      print("Error opening file.")
    for i in inf.readlines(): 
      mystring = i.strip().split('|')
      CardCatalog.append(Book(*mystring))
    inf.close()
    
    inf = open('periodic.txt','r')
    if inf.closed:
      print("Error opening file.")
    for i in inf.readlines():
      mystring = i.strip().split('|')
      CardCatalog.append(Periodical(*mystring))
    inf.close()

    inf = open('video.txt','r')
    if inf.closed:
      print("Error opening file.")
    for i in inf.readlines():
      mystring = i.strip().split('|')
      CardCatalog.append(Video(*mystring))
    inf.close()

    inf = open('film.txt','r')
    if inf.closed:
      print("Error opening file.")
    for i in inf.readlines():
      mystring = i.strip().split('|')
      CardCatalog.append(Film(*mystring))
    inf.close()

  def search_title(self, search):
    result_list = list()
    for i in CardCatalog:
      found = i.compare_title(search)
      if found:
        result_list.append(i)
    return result_list

  
  def search_call_no(self, search):
    result_list = list()
    for i in CardCatalog:
      found = i.compare_call_no(search)
      if found:
        result_list.append(i)
    return result_list

  def search_subject(self, search):
    result_list = list()
    for i in CardCatalog:
      found = i.compare_subject(search)
      if found:
        result_list.append(i)
    return result_list

  def search_other(self, search):
    result_list = list()
    for i in CardCatalog:
      found = i.compare_other(search)
      if found:
        result_list.append(i)
    return result_list
