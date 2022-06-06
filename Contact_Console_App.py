
class Contact:
    def __init__(self):
        pass
        #self.contacts = {}

    def add_Contact(self, name, number):
        self.name = name
        self.number = number
        with open('contacts.txt', 'a') as f:
            for i in range(58,127):
                if chr(i) in self.number:
                    print(f"Must be a valid phone number!\nAnd I'm realy sorry, {self.name} couldn\'t be added")
            f.write(f'{self.name} - {self.number},')    

    def delete_Contact(self, name):
        self.name = name
        with open('contacts.txt') as f:
            text = f.read()
        if self.name in text:
            text = text.replace(self.name, '')
            for i in range(len(self.contacts)):
                if self.name in self.contacts:
                    del self.contacts[self.name]
                    info = f.read()
                    new = info.replace(self.name, '')
                    f.write(new)
                    return f'{self.name} has been succesfully deleted'

    def search_Contact(self, name):
        self.name= name
        with open('contacts.txt') as f:
            text = f.read()
        if self.name in text:
            return True
        else:
            return False

    def update_Contact(self,name, new_name):
        self.name, self.new_name = name, new_name
        with open('contacts.txt') as f:
            text = f.read()
            if self.name in text:
                text = text.replace(self.name, self.new_name)
            else:
                print(f'{self.name} not found in the database!')
        with open('contacts.txt', 'w') as f:
            f.write(text)

    def sort_Contacts(self):
        self.new_Contacts = {}
        with open('contacts.txt') as f:
            text = f.read()
        text = text[0:-1]
        with open('contacts.txt', 'w') as f:
            f.write(text)


        with open('contacts.txt') as f:
            text = f.read()
        result = dict((a.strip(), int(b.strip()))
            for a, b in (element.split('-')
                for element in text.split(', ')))
        sort_details = {}
        for i in sorted(result):
            sort_details[i] = result[i]
        for i in result:
            print(f'\n{i} -> {result[i]}', end='')

    def show_Contacts(self):
        with open('contacts.txt') as f:
            text = f.read()
        print(f'\n{text}', end='')


