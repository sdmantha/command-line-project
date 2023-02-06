from peewee import *


# connection to the database
db = PostgresqlDatabase('contacts', user='samanthadelacruz', password='', host='localhost', port=5432)                  
db.connect()


class BaseModel(Model):
    class Meta:
        database = db

class Contacts (BaseModel):
    name = CharField ()
    phone_number= CharField ()
    email= CharField ()

# db.drop_tables([Contacts])
# db.create_tables([Contacts])

# # pre inserted  contacts, no need for the seed file to be imported
# sam = Contacts(name='Sam Delacruz', phone_number= 8034460449, email= 'sdangelcake@gmail.com')
# sam.save()
# antuan = Contacts(name='Ant Delacruz', phone_number= 8034460450, email= 'actuan@gmail.com')
# antuan.save()
# chu = Contacts(name='Chu Delacruz', phone_number= 8034460451, email= 'cdu@gmail.com')
# chu.save()
# ariel = Contacts(name='Ariel Delacruz', phone_number= 8034460452, email= 'adiel@gmail.com')
# ariel.save()

# how we are going to add all the contacts from the table 

find_contact= []

all_contacts= Contacts.select()
    
# beginning contacts function that 
def contacts():
    reply= input ('Welcome to your contacts, if you want to see them all type (all), if you want to create a new contact type "new", if you want to find a specific contact, type "search"' )
    if reply == "all":
        # all_contacts = []
        # contacts = Contacts.select()
        # for c in contacts:
        #     one_contact=[c.name, c.email, c.phone_number, c.email]
        #     all_contacts.append(one_contact)
        for contact in Contacts:
            print(f"{contact.name}")
        print(contacts)
        # for index in range(len(contacts)):
        #     names = contacts[index][0]
        #     show_names = input (f'Your recent contacts are \n {names}')
    elif reply == 'new':
        name = input('What is their name?')
        number = input('What is their phone number?')
        email = input('What is their email?')
        new_contact = Contacts(name=name, phone_number=number, email=email)
        new_contact.save()
        print(new_contact)
        contacts()
    elif reply == 'search':
        name = input('Please enter their full name.')
        for contact in all_contacts:
            if name == contact.name:
                print(f"{contact.name} {contact.email}")
    else:
        print('Ok looks like you do not want to do anything with your contacts.')
    
contacts()
    # def create_new ():
    #     user_input= input(f'Who do you want to add to your contacts? Type "yes" or "exit"')
    #     if user_input== "yes" or "YES" or "Yes":


    #      # Store new card into Card table
    #     added_question = Card(front={user_question}, back={user_answer})
    #     added_question.save()
    #     # Append new card to all_cards list
    #     new_question=[user_question, user_answer]
    #     all_cards.append(new_question)













# rocky = Contacts(name='Rocky', phone_number= 1234567890, email='rocky@gmail.com')
# rocky.save()

# grab = Contacts.get(Contacts.name == 'Rocky')


# grab = Contacts.get(Contacts.name == 'Rocky')
# # run this in the lib (virtual) file
# print (grab.name)
# print(f'{grab.name} email adress is  {grab.email}')




# get_lucy= Contacts.get(Contacts.name == 'Lucy')
# get_lucy.email = Contacts.get('lucy@gmail.com')
# get_lucy.save()


# rocky.delete_instance()

