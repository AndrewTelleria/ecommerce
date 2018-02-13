'''
Shell session 1
python manage.py shell
'''

from tags.models import Tag

qs = Tag.objects.all()
print(qs)
t = Tag.ojects.last()
t.title
t.slug

t.products
"""
Returns:
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x105e91c88>
"""

t.products.all()
"""
This is an actual queryset of products
Much like Product.objects.all(), but in this case it's ALL of the products that are related to the "T-shirt" tag
"""
black.products.all().first()
"""
returns the first instance, if any
"""
exit()

"""
Shell session 2
python manage.py shell
"""
from products.models import Product


qs = Product.objects.all()
print(qs)
tshirt = qs.first()
tshirt.title
tshirt.description

tshirt.tag
"""
Raises an error because the Product model doesn't have a field "tag"
"""

tshirt.tags
"""
Raises an error because the Product model doesn't have a field "tag"
"""

tshirt.tag_set
"""
This works because the Tag model has the "prodcuts" field with the ManyToMany to Product
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x105e76358>
"""

tshirt.tag_set.all()
"""
Returns an actual Queryset of the Tag model related to this project
<QuerySet [<Tag: T-shirt>, <Tag: Red>, <Tag: Black>, <Tag: Tshirt>, <Tag: T-shirt>]>
"""

tshirt.tag_set.filter(title__icontains='tshirt')

