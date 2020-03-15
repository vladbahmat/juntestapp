from django.db import models

class Operation(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='Description')
    keywords = models.CharField(max_length=120, default='Key words')
    aim = models.FileField(null=True, blank=True)
    content = models.TextField()
    #visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        ordering = ["-id", "-timestamp"]
        abstract=True

    def __unicode__(self):
        return self.name
 
    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return "/%s/" %(self.id)


class Sort(Operation):
    CH_LIST=[('Buble','Buble'),('Merge','Merge'),('Inserts','Inserts')]
    sort_type=models.CharField(max_length=20,choices=CH_LIST,default='Buble')
 
    

