def spam():
    #global eggs
    print(eggs) #this will cause an error
    eggs = 'spam local'
eggs = 'global'
spam()