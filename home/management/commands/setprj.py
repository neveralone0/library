from home.models import Category, Product, SpecialProduct
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create random users'

    # def add_arguments(self, parser):
    #     parser.add_argument('total', type=int, help='Indicates the number of users to be created')
    #
    #     # Optional argument
    #     parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        check = Category.objects.all()
        check2 = Product.objects.all()
        check3 = SpecialProduct.objects.all()
        if not check:
            Category.objects.create(
                name='default',
                slug='default'
            )
        if not check2:
            c = Product.objects.create(
                name='default book',
                slug='def-book',
                description='the book',
                price=99,
                image='Media/1014.jpg',
            )
            c.category.add(1)
            id = c.id
            c.save()
        if not check3:
            SpecialProduct.objects.create(
                spc=id
            )
