from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

# Create your models here.
class ProductManager(models.Manager):
    def createVal(self, postData):
        results = {'status': False, 'errors': []}

        if not postData['product_name']:
            results['errors'].append('Please add an item/product.')
            results['status'] = True

        if len(postData['product_name']) < 3:
            results['errors'].append('Product must be at least 3 characters long.')
            results['status'] = True

        # if results['status'] == False:
        #     if len(self.filter(product_name = postData['product_name'])) == 0:
        #     #     results['product'] = self.create(product_name = postData['product_name'])
        #     # else:
        #         results['errors'].append('Item/Product has already been added to the list.')
        #         results['status'] = True

        return results

class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    added_by = models.ManyToManyField(User, related_name = 'users')
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ProductManager()
