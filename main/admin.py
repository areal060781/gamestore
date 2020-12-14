from django.contrib import admin

from .models import GamePlatform
from .models import Game
from .models import PriceList
from .models import ShoppingCart
from .models import ShoppingCartItem

admin.autodiscover()

admin.site.register(GamePlatform)
admin.site.register(Game)
admin.site.register(PriceList)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)

# Register your models here.
