def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    list_of_names = []
    
    for name in names:
        list_of_names.append(f"Hello, my name is {name}.")
        
    return list_of_names

def assign_rooms(names):
    list_of_room_assignments = []
    
    for name in names:
        list_of_room_assignments.append(f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!")
    
    return list_of_room_assignments

def printer(names):
    # output of batch_badge_creator
    # output of assign_rooms
    # loop thru each list
    batch_list = batch_badge_creator(names)
    
    for name in batch_list:
        print(name)
        
    room_list = assign_rooms(names)
    
    for string in room_list:
        print(string)
    
