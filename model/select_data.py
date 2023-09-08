from main import session
from models import Device, SceneDevice
from sqlalchemy import select


statement = select(SceneDevice)

result = session.scalars(statement).all()

for i in result:
    print(i)
