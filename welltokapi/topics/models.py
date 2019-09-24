from django.db import models
import uuid
# Create your models here.

def generate_topic_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique topic id

class Topic(models.Model):
    topic_id = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.topic_id, self.title)

    def save(self, *args, **kwargs):
        if len(self.topic_id.strip(" "))==0:
            self.topic_id = generate_topic_id()

        super(Topic, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-created_at"]