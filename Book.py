#Book
from Media import Media

class Book(Media):
  def __init__ (self, callNum, title, subject, auth, desc, pub, cty, yer, ser, note):
    super().__init__(callNum, title, subject, note)
    self.m_author = auth
    self.m_description = desc
    self.m_publisher = pub
    self.m_city = cty
    self.m_year = yer
    self.m_series = ser
  def display(self):
    print("===========================Search Results============================\n")
    print("Media Type:    Book\n")
    super().display()
    print("Author:      ",self.m_author)
    print("Description: ",self.m_description)
    print("Publisher:   ",self.m_publisher)
    print("City:        ",self.m_city)
    print("Year:        ",self.m_year)
    print("Series:      ",self.m_series)

  def compare_other(self,search_other):
    found1 = self.m_description.find(search_other)
    found2 = self.m_notes.find(search_other)
    found3 = self.m_year.find(search_other)

    if(found1 == -1 and found2 == -1 and found3 == -1):
      return False
    else:
      return True


