

#     PROJECT CODE 

print('********ENQUIRY SYSTEM********')




l=[]




def viewlist():

      for i in l:
                print(f"\nname-->{i[0]} DOB-->{i[1]}  Gmail-->{i[2]}")

def add_data():
                while True:
                             x=input("\nenter your Name,DOB and Gmail").split(",")
                             l.append(x)
                             y=input("\nanymore: yes/no")
                             if y=="yes":
                                             pass
                             else:
                                             break

                                

def search_data():
                name=input("\nenter the name to search")
                


                for i in l:
                                if name==i[0]:
                                                print('!!! name found !!!')
                                                print(f"\nname-->{i[0]} DOB-->{i[1]}  Gmail-->{i[2]}")
                                                break

                else:
                                print('!!!not Found!!!')
                                
def end():
                print("\npress enter key to exit")
                exit()

while True:

  
  print("_________________________")
  print("                         ")
  print("Options are given plzzzz choose any:")
  print("\n1.add Data")
  print("2.view Data")
  print("3.search data")
  print("4.Exit")
  ch=input('\nenter the option')
  if ch=='1':
                add_data()
  elif ch=='2':
                viewlist()
  elif ch=='3':
                search_data()

  elif ch=='4':
                end()

  else:
                  print('wrong input')
