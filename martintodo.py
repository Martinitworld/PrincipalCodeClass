mtodolist = ['buy my christmas lists','need to clean my room','get my grocery','say hi to Frank']

print(mtodolist)
#print(len(mtodolist))

print('This is my to do for the day')

print(f' {len(mtodolist)} thing(s) left to do')
for i in mtodolist:
  print(i)
  
  add = ""
remove = ""
def addremove():
  print ("Would you like to add or remove an item?\n")
 

def addlist():
  add = input("What would you like to do in your to do list? \n")
  todolist.append(f"{add}\n")

def removelist():
  remove = input("What would you like to remove from your to do list? \n")
  todolist.remove(f"{remove}\n")





def todolist():
  print (f"To do list: \n")

while todolist > 0:
  todolist()
  
  addremove()
  
  answer = input()
  
  if answer == "add":
    add()
