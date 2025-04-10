import os
import json

def load_file(filename):
    if os.path.exists(filename):
        with open(filename,'r+')as f:
            f_object = json.load(f)
            return f_object                         
    else :
        return []

def save_file(f_object,filename):
    with open(filename, "w") as file:
        json.dump(f_object, file, indent=4)    
    pass

def show_item(f_object):
    if not f_object:
        print('the list is empty')
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(f_object, 1):
            print(f"{idx}. {task['title']} - {task['status']} ")
    pass
def add_item(f_object):
    title_ = input(('enter the title '))
    status = input('enter the status pending/Done ')
    
    item_ = {
        'title':title_,
        'status':status
    }
    f_object.append(item_)    
    pass       

def edit_item(f_object):
    itm = int(input('select the list item to edit '))-1
    print(f'you have selected {f_object[itm]}')
    count = 1
    for atribs,val in f_object[itm].items():
        print(count,atribs,val)
        count +=1
        pass        
    option = int(input('select the attributes to update '))
    if option == 1:
        print(f'title is {f_object[itm]['title']}')
        title = input('enter the value to hte updated ')
        f_object[itm]['title'] = title
        print(f'titlle is updated{title}')        
    elif option == 2:
        print(f'status is {f_object[itm]['status']}')
        status = input('enter the status ')
        f_object[itm]['status'] = status
        print(f'status is updated to {status}')
        pass                

def Delete_item(f_object,delete_i):           
    try:
        deleted_item = f_object.pop(delete_i-1)        
        print(f"Task '{deleted_item}' removed!")
    except IndexError:
        print('invalid task number')
        pass
    pass    
    
def clear_list(f_object):
    f_object.clear()
    pass

def main():
    intro =  """
Select from the following options
1). Show List
2). Add Item
3). Edit Item
4). Delete Items
5). Clear list
""" 
    filename = 'rason4.json'
    f_object = load_file(filename)
    is_running = True
    while is_running:
        print(intro)
        try:
            val = int(input("enter the corresponding vallue :"))
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('incorrect value entered')        
        if val == 1:
            show_item(f_object)
            pass                        
        elif val == 2:
            add_item(f_object)
            save_file(f_object,filename)               
            pass
        elif val == 3:
            show_item(f_object)
            edit_item(f_object)
            save_file(f_object,filename)
            pass
        elif val == 4:
            show_item(f_object)
            delete_i = input('select the item to be removed ').strip()
            
            if delete_i.isdigit():
                Delete_item(f_object,int(delete_i))
                save_file(f_object,filename)
            pass            
        elif val == 5:
            clear_list(f_object)
            save_file(f_object,filename)
            pass                      
        elif val == 0:
            exit()
            is_running= False
        else:
            print('invalid number selected')
main()