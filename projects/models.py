from django.db import models
from django.db.models.fields import UUIDField

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    featured_image = models.ImageField(null=True ,blank=True,default='default.jpeg')
    demo_link = models.CharField(max_length=1050)
    source_code = models.CharField(max_length=1050)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag',blank=True)#we use a string because the Tag is below in m to m relationship
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True,editable=False)
    #id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    def __str__(self):
       return self.title


class Review(models.Model):
    vote_type = (
        ('up','up'),
        ('down','down'),
    )
    #owner = 
    Project = models.ForeignKey(Project,on_delete = models.CASCADE,null=True,blank=True)
    body=models.TextField(null=True,blank=True)
    value = models.CharField(max_length=50,choices=vote_type)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
       return self.value

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
       return self.name