#Film
from Media import Media

class Film(Media):

  def __init__ (self, callNum, title, subject, director, note, year):

    super().__init__(callNum, title, subject, note)
    self.m_director = director
    self.m_year = year

  def display(self):
    print("===========================Search Result===============================\n")
    print("Media type:     Film\n")
    super().display()
    print("Director:       ",self.m_director)
    print("Year:           ",self.m_year)

  def compare_other(self, search_other):
    found1 = self.m_notes.find(search_other)
    found2 = self.m_director.find(search_other)
    found3 = self.m_year.find(search_other)
    if found1 == -1 and found2 == -1 and found3 == -1:
      return False
    else:
      return True

