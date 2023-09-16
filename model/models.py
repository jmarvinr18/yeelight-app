from typing import Any
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Boolean
import json


class Base(DeclarativeBase):
    pass


class Device(Base):
    __tablename__ = 'devices'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=True)
    model: Mapped[str] = mapped_column(nullable=True)
    ip: Mapped[str] = mapped_column(nullable=False)
    port: Mapped[int] = mapped_column(nullable=False)
    capabilities: Mapped[str] = mapped_column(Text, nullable=False)
    power: Mapped[bool] = mapped_column(Boolean, nullable=False)
    brightness: Mapped[float] = mapped_column(nullable=False)
    hue: Mapped[int] = mapped_column(nullable=True)
    saturation: Mapped[int] = mapped_column(nullable=True)
    color_temperature: Mapped[int] = mapped_column(nullable=True)

    def __init__(self,
                 name="",
                 ip="",
                 port=0,
                 model="",
                 capabilities="",
                 power=False,
                 brightness=100.0,
                 hue=0,
                 saturation=0,
                 color_temperature=0,
                 ):
        self.name = name
        self.ip = ip
        self.port = port
        self.model = model
        self.capabilities = capabilities
        self.power = power
        self.brightness = brightness
        self.hue = hue
        self.saturation = saturation
        self.color_temperature = color_temperature


class SceneDevice(Base):
    __tablename__ = 'scene_devices'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(
        ForeignKey('devices.id'), nullable=False)
    scene_id: Mapped[int] = mapped_column(
        ForeignKey('scenes.id'), nullable=False)
    capabilities: Mapped[str] = mapped_column(Text, nullable=False)
    power: Mapped[bool] = mapped_column(Boolean, nullable=False)
    brightness: Mapped[float] = mapped_column(nullable=False)
    hue: Mapped[int] = mapped_column(nullable=True)
    saturation: Mapped[int] = mapped_column(nullable=True)
    color_temperature: Mapped[int] = mapped_column(nullable=True)

    def __repr__(self):
        return f'SceneDevice({self.id},{self.device_id},{self.scene_id})'


class Scene(Base):
    __tablename__ = 'scenes'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    status: Mapped[str]
