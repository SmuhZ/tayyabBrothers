from .models import Customer,Supplier,Items,Order,OrderDetails
from django.forms import ModelForm


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"


class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

class OrderDetailsForm(ModelForm):
    class Meta:
        model = OrderDetails
        fields="__all__"


