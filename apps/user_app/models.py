from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': False, 'errors': []}

        if len(postData['name']) < 3:
            results['errors'].append('Name must be at least 3 characters.')
            results['status'] = True

        if len(postData['username']) < 3:
            results['errors'].append('Username must be at least 3 characters.')
            results['status'] = True

        if len(postData['password']) < 8:
            results['errors'].append('Password must be at least 8 characters.')
            results['status'] = True

        if postData['password'] != postData['con_password']:
            results['errors'].append('Password must match.')
            results['status'] = True

        if results['status'] == False:
            if len(self.filter(username = postData['username'])) == 0:
                hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                results['user'] = self.create(name = postData['name'], username = postData['username'], date_hired = postData['date_hired'], password = hashed)
            else:
                results['errors'].append('User already exists.')
                results['status'] = True
        print results
        return results

    def loginVal(self, postData):
        results = {'status': False, 'errors': [], 'user': None}
        user = self.filter(username = postData['username'])

        if len(user) < 1 or not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            results['errors'].append('Something went wrong. Check your login credentials and try again.')
            results['status'] = True
        else:
            results['user'] = user[0]

        return results

class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 200)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
