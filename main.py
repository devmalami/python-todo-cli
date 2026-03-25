# A To-Do list app

# Features:
# Add tasks → store new items
# View tasks → display all items
# Delete tasks → remove specific item

my_tasks = []

while True:
    print('=== TO-DO LIST APP ===\n')
    print('1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit')
    
    try:
        option = int(input('\nChoose an option: '))
            
        if option == 1:
            new_task = input('Enter your task: ').strip()
            if new_task:
                print('✅ Task added successfully!\n')
                my_tasks.append(new_task)
            else:
                print('Please add a task ❌\n')
            
        elif option == 2:
            if not my_tasks:
                print('No tasks yet. Add something')
            for index, task in enumerate (my_tasks, start=1):
                print(f'{index}. {task}')
            print('')    
        elif option == 3:
            print('=== Delete Tasks ===')
        
            if not my_tasks:
                print('No task to delete. Add tasks 📝\n')
                continue
            for index, task in enumerate (my_tasks, start=1):
                print(f'{index}. {task}')
            try:        
                remove_task = int(input('Choose a task you want to delete: '))
                adj_remove_task = remove_task - 1 # Adjusted remove_task to match 0 indexing    
                if 1 <= remove_task <= len(my_tasks):
                    del my_tasks[adj_remove_task]
                    print('Task deleted successfully!\n')
                else:
                    print('Enter a valid option\n')
                    continue 
            except ValueError:
                print('Enter a number only\n')    
        elif option == 4:
            break         
        else:
            print('Please choose option from 1 - 4\n')        
    except ValueError:
        print('Reply with an option number only\n')    
