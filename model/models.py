from typing import Any
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text


class Base(DeclarativeBase):
    pass


class Device(Base):
    __tablename__ = 'devices'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ip: Mapped[str] = mapped_column(nullable=False)
    port: Mapped[int] = mapped_column(nullable=False)
    capabilities: Mapped[str] = mapped_column(Text, nullable=False)

    def __init__(self, ip, port, capabilities):
        self.ip = ip
        self.port = port
        self.capabilities = capabilities

    def __repr__(self):
        return f'Device({self.id},{self.ip},{self.port},{self.capabilities})'


class SceneDevice(Base):
    __tablename__ = 'scene_devices'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(
        ForeignKey('devices.id'), nullable=False)
    scene_id: Mapped[int] = mapped_column(
        ForeignKey('scenes.id'), nullable=False)

    def __repr__(self):
        return f'SceneDevice({self.id},{self.device_id},{self.scene_id})'


class Scene(Base):
    __tablename__ = 'scenes'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    status: Mapped[str]
