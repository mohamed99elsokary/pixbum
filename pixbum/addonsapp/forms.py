
from django.forms import ModelForm
from django.forms.widgets import TextInput

from pixbum.addonsapp.models import SectionContent, SliderPicture


class SliderPictureForm(ModelForm):
    class Meta:
        model = SliderPicture
        fields = "__all__"
        widgets = {
            "button_hex_color": TextInput(attrs={"type": "color"}),
            "button_text_color": TextInput(attrs={"type": "color"}),
            "color": TextInput(attrs={"type": "color"}),
        }


class SectionContentForm(ModelForm):
    class Meta:
        model = SectionContent
        fields = "__all__"
        widgets = {
            "button_hex_color": TextInput(attrs={"type": "color"}),
            "button_text_color": TextInput(attrs={"type": "color"}),
            "color": TextInput(attrs={"type": "color"}),
        }
