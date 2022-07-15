from views import *

urlpatterns = [
    ('cars/', car_listing),
    ('car-create/', car_create),
    ('car-retrieve/', car_retrieve),
    ('car-delete/', car_delete),
    ('car-update/', car_update),
]