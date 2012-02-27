from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import DictField
from djangotoolbox.fields import EmbeddedModelField

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

# Entity model.  We'll basically extend this instead of making it from scratch.
class Entity(models.Model):
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()
    entity_type = models.CharField(max_length=255)
    data = DictField()

# IRC Log model.  Contains checks to prevent duplicates and some custom formatting for the timeline display
class IrcLog(Entity):
    # create a custom thingy here
    class MongoMeta:
        #unique_together = (('created_on', 'data'))