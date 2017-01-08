#Video class

from Media import Media

class Video(Media):

  def __init__ (self, callNum, title, subject, note, desc, dist, series, label):
    super().__init__(callNum, title, subject, note)
    self.m_desc = desc
    self.m_distributor = dist
    self.m_series = series
    self.m_label = label

  def display(self):
    print("===============================Search Results===============================\n")
    print("Media Type:     Video\n")
    super().display()
    print("Description:   ",self.m_desc)
    print("Distributor:   ",self.m_distributor)
    print("Series:        ",self.m_series)
    print("Label:         ",self.m_label)

  def compare_other(self,search_other):
    found1 = self.m_desc.find(search_other)
    found2 = self.m_notes.find(search_other)
    found3 = self.m_distributor.find(search_other)
    if found1 == -1 and found2 == -1 and found3 == -1:
      return False
    else:
      return True

