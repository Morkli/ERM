from import_export import resources
from main.models import Members


class MemberResource(resources.ModelResource):
    class Meta:
        model = Members
        import_id_fields = ('member_id',)

