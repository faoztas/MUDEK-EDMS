from django.forms import ModelForm
from edms.models import Requested_Documents


class Requested_DocumentsForm(ModelForm):

    class Meta:
        model = Requested_Documents
        fields = ['d_name','d_bool']
