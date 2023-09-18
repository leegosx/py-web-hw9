from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    fullname = StringField(required=True, max_length=100)
    born = StringField(required=True, max_length=50)
    bio = StringField(required=True)

class Quotes(Document):
    tags = StringField(required=False)
    author = ReferenceField(Author, reverse_delete_rule=2)
    text = StringField(required=True)