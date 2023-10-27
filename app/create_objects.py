from app.models import Warehouse
from app.serialaizer import WarehouseSerializer

warehouse = Warehouse.objects.create(name='РРЦ на Днепровской')
s = WarehouseSerializer(instance=warehouse)
print(s.data)