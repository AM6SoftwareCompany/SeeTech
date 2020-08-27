from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    ShopView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    index,

    PView,
    TBView,
    PAView,
    CView,
    LPView,
    CAView,
    PSView,
    TView,
    SRView,
    PJView,
    ADView,
    TAView,
    CMView,
    MWView,
    WWView,
    MAView,
    WAView

)

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    path('shop/P/', PView.as_view(), name='P'),
    path('shop/TB/', TBView.as_view(), name='TB'),
    path('shop/PA/', PAView.as_view(), name='PA'),
    path('shop/C/', CView.as_view(), name='C'),
    path('shop/LP/', LPView.as_view(), name='LP'),
    path('shop/CA/', CAView.as_view(), name='CA'),
    path('shop/PS/', PSView.as_view(), name='PS'),
    path('shop/T/', TView.as_view(), name='T'),
    path('shop/SR/', SRView.as_view(), name='SR'),
    path('shop/PJ/', PJView.as_view(), name='PJ'),
    path('shop/AD/', ADView.as_view(), name='AD'),
    path('shop/TA/', TAView.as_view(), name='TA'),
    path('shop/CM/', CMView.as_view(), name='CM'),
    path('shop/MW/', MWView.as_view(), name='MW'),
    path('shop/WW/', WWView.as_view(), name='WW'),
    path('shop/MA/', MAView.as_view(), name='MA'),
    path('shop/WA/', WAView.as_view(), name='WA')
    
]


