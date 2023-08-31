from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from django.utils import timezone




class Book(models.Model):
    book_name = models.CharField(max_length=150)
    author_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=2000)

    class Meta:
        unique_together = ('book_name','author_name')        
    
    def __str__(self):
        return self.book_name
    


class IssuedItem(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today(),blank=False)
    return_date = models.DateField(blank=True,null=True)

    # property to get book name
    @property
    def book_name(self):
        return self.book_id.book_name
    
    # property to get author name
    @property
    def username(self):
        return self.user_id.username
    
    def __str__(self):
        return self.book_id.book_name + ' issued by ' + self.user_id.first_name + ' on ' + str(self.issue_date) 




class Author(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
   

    # def __str__(self):
    #     return f"{self.name} - {self.book.book_name}"
    
