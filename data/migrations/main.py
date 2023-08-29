import sqlite3


class Model():

    def __init__(self, name="", column=()) -> None:

        self.conn = sqlite3.connect('data/data.db')
        self.name = name
        self.column = column

    def create(self, *args):

        insert = f'''INSERT INTO {self.name} {self.column}
                           VALUES {args}'''
        cursor = self.conn.cursor()

        cursor.execute(insert)
        self.conn.commit()
        self.conn.close()

    def update():
        print("updated")
        pass

    def delete():
        print("deleted")
        pass


class Devices(Model):

    name = "devices"
    db_columns = "(ip STRING, port INTEGER, capabilities TEXT)"
    columns = "(ip, port, capabilities)"

    def __init__(self) -> None:
        super().__init__(self.name, self.columns)


class Scenes(Model):
    name = "scenes"
    db_columns = "(id STRING, name STRING, status STRING)"
    columns = "(id, name, status)"

    def __init__(self) -> None:
        super().__init__(self.name, self.columns)


class SceneDevices(Model):
    name = "scene_devices"
    db_columns = "(id STRING, scene_id STRING)"
    columns = "(id, scene_id)"

    def __init__(self) -> None:
        super().__init__(self.name, self.columns)


class Migration:

    tables = (
        Devices,
        Scenes,
        SceneDevices,
    )


dev = Devices()
dev.create("123.412.123", 8000, "{asdf: aesd, adswer: aewer}")
# dev.update()
# dev.delete()
