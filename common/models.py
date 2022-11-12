from django.db import models

# we do not want to put this model into DB -> we would like this model to be used by other app (models)
class CommonModel(models.Model):

    """ Common Model Definition """

    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add -> will set the value when the object was created first
    updated_at = models.DateTimeField(auto_now=True) # auto_now -> will set the value when the object was saved (updated)

    class Meta:
        # need to tell Django that we do not want this to be shown in DB
        abstract = True # this model will be never used in actual db