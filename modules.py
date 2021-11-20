import converters
from converters import kg_to_lbs, Mammal

print(kg_to_lbs(65))

Dog = Mammal()
Dog.talk()

import ecommerce.shipping
from ecommerce import shipping
from ecommerce.shipping import *  # this imports all the classes and functions in that module
from ecommerce.shipping import calc_shipping

ecommerce.shipping.calc_shipping()
shipping.calc_shipping()
calc_shipping()