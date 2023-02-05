from peewee import *

db = PostgresqlDatabase('contact', user='postgres', password='123', host='localhost', port=5432)                  

db.connect()


class BaseModel(Model):
    class Meta:
        database = db

class Contacts (BaseModel):
    name = CharField ()
    phone_number= CharField ()
    email= CharField ()

db.drop_tables([Contacts])
db.create_tables([Contacts])


rocky = Contacts(name='Rocky', phone_number= 1234567890, email='rocky@gmail.com')
rocky.save()

grab = Contacts.get(Contacts.name == 'Rocky')


grab = Contacts.get(Contacts.name == 'Rocky')
# run this in the lib (virtual) file
print (grab.name)
print(f'{grab.name} email adress is  {grab.email}')




get_lucy= Contacts.get(Contacts.name == 'Lucy')
get_lucy.email = Contacts.get('lucy@gmail.com')
get_lucy.save()


rocky.delete_instance()

