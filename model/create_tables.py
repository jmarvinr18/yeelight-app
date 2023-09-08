from models import Base, Device, Scene, SceneDevice
from connect import engine


print("CREATING TABLES >>>> ")
Base.metadata.create_all(bind=engine)
