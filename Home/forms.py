from typing import Any

from django.forms import ModelForm, forms
from django.core.exceptions import ValidationError

from .models import Warehouse


class WarehouseForm(ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#121416] focus:outline-0 focus:ring-0 border border-[#dde0e3] bg-white focus:border-[#dde0e3] h-14 bg-[image:--select-button-svg] placeholder:text-[#6a7581] p-[15px] text-base font-normal leading-normal'})

    class Meta:
        model = Warehouse
        # fields = '__all__'
        exclude = ('manager',)


    def clean_capacity(self):
        capacity = int(self.data['capacity'])
        location = self.data['location']

        if location == "aswan" and capacity > 20000:
            raise ValidationError("You can't have more than 20000 Capacity")

        return capacity
