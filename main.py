#from ModuleName import attribute
from SearchEngine import SearchEngine
import sys
import os

searchEngineObj = SearchEngine()

#end = 'false'

def main():
  end = 'false'
  while end == 'false':
    print("=======================================================\n")
    print("Enter Type of Search:\n")
    print("Search by:")
    print("Title")
    print("Call number")
    print("Subject")
    print("Other")
    print("Exit")
    print("=======================================================\n")
    optiontype = str(input())

    if optiontype == "Exit":
      end = "true"
    if optiontype == 'Title' or optiontype == 'Call number' or optiontype == 'Subject' or optiontype == 'Other':
      print("=======================================================\n")
      print("Please enter the string to be searched")
      print("=======================================================\n")
    
      search = str(input())
    
      if search != '' and optiontype != '':
        final = list()
        if optiontype == "Title":
          final = searchEngineObj.search_title(search)
        elif optiontype == "Call number":
          final = searchEngineObj.search_call_no(search)
        elif optiontype == "Subject":
          final = searchEngineObj.search_subject(search)
        elif optiontype == "Other":
          final = searchEngineObj.search_other(search)
    
        size = len(final)
        #print(size)
        if size != 0:
          print("=======================================================\n")
          print(size,"Entries found that matches '",search, "' when searched by '",optiontype,"' ")
          for i in final:
            i.display()
          print("=======================================================\n")
          print(size,"Entries found that matches '",search, "' when searched by '",optiontype,"' ")
        else:
          print("=======================================================\n")
          print("No match found.")
    else:
      if optiontype == "Exit":
        print("=======================================================\n")
        print("Exiting the Library application")
        print("=======================================================\n")
      else:
        print("=======================================================\n")
        print("Not a valid search")
        print("=======================================================\n")
if __name__ == "__main__":
  main()
