from models import Device
from main import session


device = Device("112.12.14", 123, "asdfajkwerwer")

session.add(device)
session.commit()
