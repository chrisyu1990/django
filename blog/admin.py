from django.contrib import admin
from .models import Session
from .models import Speaker
from .models import Location
from .models import Timeslot
from .models import Floor
from .models import Beacon


admin.site.register(Session)
admin.site.register(Speaker)
admin.site.register(Location)
admin.site.register(Timeslot)
admin.site.register(Floor)
admin.site.register(Beacon)