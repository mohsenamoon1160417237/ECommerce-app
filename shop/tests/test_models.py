from django.test import TestCase
from shop.models import Category , Product , ProductAttribute , ProductDetail
from django.db import models
from django.utils.text import slugify
from decimal import Decimal
import tempfile


class CategoryTest(TestCase):

    def setUp(self):

        self.category = Category.objects.create(name='clothes',
                                                description='clothes')
        self.category.save()
    
    def test_model(self):

        category = Category.objects.get(id=1)
        self.assertEqual(category.name , 'clothes')
        self.assertEqual(category.name , 'clothes')
        self.assertEqual(category.slug , slugify('clothes'))


class ProductTest(TestCase):

    def setUp(self):

        category = Category.objects.create(name='clothes',
                                           description='clothes')
        category.save()

        self.image = tempfile.NamedTemporaryFile(suffix='.jpg').name

        product = Product.objects.create(category=category,
                                         name='scarf',
                                         image=self.image,
                                         description='high quality',
                                         manufacturer='Mohsen',
                                         price='120.00'
                                         )
        
        product.save()

    def test_model(self):

        product = Product.objects.get(id=1)
        category = Category.objects.get(id=1)
        image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        self.assertEqual(product.category , category)
        self.assertEqual(product.name , 'scarf')
        self.assertEqual(product.slug , slugify('scarf'))
        self.assertEqual(product.description , 'high quality')
        self.assertEqual(product.manufacturer , 'Mohsen')
        self.assertEqual(product.price , Decimal('120.00'))
        self.assertEqual(product.image , self.image)
        self.assertTrue(product.available)       



class ProductAttributeTest(TestCase):

    def setUp(self):

        attr = ProductAttribute.objects.create(name='quality',
                                               description='high sold')

        attr.save()
    
    def test_model(self):

        attr = ProductAttribute.objects.get(id=1)
        self.assertEqual(attr.name , 'quality')
        self.assertEqual(attr.description , 'high sold')


class ProductDetailTest(TestCase):

    def setUp(self):

        category = Category.objects.create(name='clothes',
                                                description='clothes')
        category.save()

        product = Product.objects.create(category=category,
                                         name='scarf',
                                         description='high quality',
                                         manufacturer='Mohsen',
                                         price='120.00'
                                         )

        attr = ProductAttribute.objects.create(name='quality',
                                               description='high sold')

        product_detail = ProductDetail.objects.create(product=product,
                                                      attribute=attr,
                                                      value='high',
                                                      description='very well')



    
    def test_model(self):

        product_detail = ProductDetail.objects.get(id=1)
        product = Product.objects.get(id=1)
        attr = ProductAttribute.objects.get(id=1)

        self.assertEqual(product_detail.product , product)
        self.assertEqual(product_detail.attribute , attr)
        self.assertEqual(product_detail.value , 'high')
        self.assertEqual(product_detail.description , 'very well')