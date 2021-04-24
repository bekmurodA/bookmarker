class Option:
    def __init__(self,name,command,prep_call=None):
        self.name=name
        self.command=command
        self.prep_call=prep_call

    def choose(self):
        if self.name == 'Add a bookmark':
           data = self.prep_call() if self.prep_call else {}
           print("we need data")

           data['title'] = input("title: ")
           while(data['title'] == ''):
               data['title'] = input("title can't be empty: " )
           data['url'] = input("url: ")
           while(data['url'] == ''):
               data['url'] = input("url can't be empty: " )
           data['notes'] = input("notes(optional): ")
           message = self.command.execute(data)
        elif(self.name=='Delete a bookmark'):
            data = input("id of the bookmark: ")
            message = self.command.execute(data)
        else:
            data = self.prep_call() if self.prep_call else None
            message = self.command.execute(data) if data else self.command.execute()
        print(message)
    
    def __str__(self):
        return self.name

