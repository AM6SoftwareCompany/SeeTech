from django.contrib import admin
from django.contrib.auth.models import Group

from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from allauth.account.models import EmailAddress
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    # 'refund_requested',
                    # 'refund_granted',
                    'shipping_address',
                    'billing_address'
                    # 'payment',
                    # 'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address'
        # 'payment',
        # 'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received'
                   # 'refund_requested',
                   # 'refund_granted'
                   ]
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

class ItemAdmin(admin.ModelAdmin):
    view_on_site = False
    search_fields = ['title', 'description']
    list_display = ['title', 'price']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Item

admin.site.register(Item, ItemAdmin)

admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
# admin.site.register(Payment)
# admin.site.register(Coupon)
# admin.site.register(Refund)
# admin.site.register(UserProfile)
admin.site.register(Address, AddressAdmin)
 

admin.site.unregister(Group)

admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)


