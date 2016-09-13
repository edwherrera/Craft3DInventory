from service import service

order_service = service.Order()

print(order_service.get_all()[0].material.name)
