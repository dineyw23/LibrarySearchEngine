#Periodical
from Media import Media

class Periodical(Media):
  def __init__ (self, callNum, title, subject, auth, desc, pub, pub_hist, series, note, related_title, other_title, gov_doc_id):
    super().__init__(callNum, title, subject, note)
    self.m_author = auth
    self.m_description = desc
    self.m_publisher = pub
    self.m_publishingHistory = pub_hist
    self.m_series = series
    self.m_relatedTitle = related_title
    self.m_otherTitle = other_title
    self.m_gov_doc_id = gov_doc_id
  
  def display(self):
    print("=========================Search Result===============================\n")
    print("Media type:     Periodical\n")
    super().display()
    print("Author:         ",self.m_author);
    print("Description:    ",self.m_description);
    print("Publisher:      ",self.m_publisher);
    print("Publishing Hist:",self.m_publishingHistory);
    print("Series:         ",self.m_series);
    print("Related title:  ",self.m_relatedTitle);
    print("Other title:    ",self.m_otherTitle);
    print("Gov doc ID:     ",self.m_gov_doc_id);

  def compare_other(self,search_other):
    found1 = self.m_description.find(search_other)
    found2 = self.m_notes.find(search_other)
    found3 = self.m_series.find(search_other)
    found4 = self.m_relatedTitle.find(search_other)

    if found1 == -1 and found2 == -1 and found3 == -1 and found4 == -1:
      return False
    else:
      return True

