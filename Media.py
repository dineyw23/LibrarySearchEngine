#Media Class

class Media:
  def __init__ (self, callNum, title, sub, note):
    self.m_callno = callNum
    self.m_title = title
    self.m_subject = sub
    self.m_notes = note
    
  def display(self):
    print("Call number:   ",self.m_callno)
    print("Title:         ",self.m_title)
    print("Subject:       ",self.m_subject)
    print("Notes:         ",self.m_notes)
    
  def compare_call_no(self, search_callno):
    found = self.m_callno.find(search_callno)
    if found == -1:
      return False
    else:
      return True
    
  def compare_title(self, search_title):
    found =  self.m_title.find(search_title) 
    if found == -1:
      return False
    else:
      return True
    
  def compare_subject(self, search_subject):
    found = self.m_subject.find(search_subject) 
    if found == -1:
      return False
    else:
      return True
